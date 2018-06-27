import argparse
import json
import logging
import subprocess
import time
import typing


from fluent import sender


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_logger(tag: str) -> sender.FluentSender:
    try:
        logger = sender.FluentSender(tag)
        yield logger
    finally:
        logger.close()


def run_speedtest() -> (typing.Dict, int):
    try:
        logger.info("Running speedtest")
        timestamp = int(time.time())
        output = subprocess.check_output(["speedtest", "--json"]).decode("utf-8")
        results = json.loads(output)
        logging.debug("results: %s", results)
        return results, timestamp
    except Exception as e:
        logger.error("Error running speedtest: %s", e)
        return {}, 0

def loop(fs: sender.FluentSender, interval: int):
    while True:
        results, timestamp = run_speedtest()
        if results:
            if not fs.emit_with_time("laptop", timestamp, results):
                logger.error("fluent error: %s", fs.last_error)
                fs.clear_last_error()

        logger.info("Sleeping for %s", interval)
        time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="Run speedtest")
    parser.add_argument("--interval", type=int, default=5,
                        help="The number of seconds to wait between successive speedtest runs")
    parser.add_argument("--tag", type=str, default="speedtest")
    parser.add_argument("--fluent-host", type=str, default="localhost",
                       help="The hostname where the fluentd service is running")
    parser.add_argument("--fluent-port", type=int, default=24224,
                       help="The port where the fluentd service is running")
    return parser.parse_args()


def main():
    args = parse_args()
    with sender.FluentSender(args.tag, host=args.fluent_host, port=args.fluent_port) as fs:
        loop(fs, args.interval)


if __name__ == "__main__":
    main()
