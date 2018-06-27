import argparse
import fluent
import json
import subprocess
import typing


def get_logger(tag: str) -> fluent.sender.FluentSender:
    try:
        logger = sender.FluentSender(tag)
        yield logger
    finally:
        logger.close()


def run_speedtest() -> typing.Dict:
    try:
        output = subprocess.check_output(["speedtest", "--json"])).decode("utf-8")
        results = json.loads(output)
        return results
    except Exception as e:
        print("Error running speedtest:", e)
        return {}

def loop(interval: int):
    logger = get_logger("speedtest")









def parse_args():
    parser = argparse.ArgumentParser(description="Run speedtest")
    parser.add_argument("--interval", type=int, default=5,
                        help="The number of minutes to wait between successive speedtest runs")
    return parser.parse_args()


def main():
    args = parse_args()

if __name__ == "__main__":
    main()
