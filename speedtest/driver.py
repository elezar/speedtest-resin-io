#!/usr/env/bin python3

import argparse
import json
import logging
import re
import socket
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


def loop(fs: sender.FluentSender, connection_id: str, interval: int):
    while True:
        results, timestamp = run_speedtest()
        if results:
            if not fs.emit_with_time(connection_id, timestamp, results):
                logger.error("fluent error: %s", fs.last_error)
                fs.clear_last_error()

        logger.info("Sleeping for %s", interval)
        time.sleep(interval)


def parse_args():
    parser = argparse.ArgumentParser(description="Run speedtest")
    parser.add_argument("--interval", type=int, default=5,
                        help="The number of seconds to wait between successive speedtest runs")
    parser.add_argument("--fluent-host", type=str, default="localhost",
                       help="The hostname where the fluentd service is running")
    parser.add_argument("--fluent-port", type=int, default=24224,
                       help="The port where the fluentd service is running")

    parser.add_argument("--connection-id", type=str,
                        help="An ID to indentify the connection being tested")

    return parser.parse_args()


def sanitize(hostname: str) -> str:
    return re.subn("[\s\.]+", "", hostname.lower())[0]


def get_connection_id(args_id: str) -> str:
    if args_id and args_id.lower() != "auto":
        return sanitize(args_id)

    results, _ = run_speedtest()

    isp_or_hostname = results["server"].get("isp") if "server" in results else None

    if not isp_or_hostname:
        isp_or_hostname = socket.gethostname()

    return sanitize(isp_or_hostname)


def main():
    args = parse_args()

    logger.info("Args: %s", args)

    connection_id = get_connection_id(args.connection_id)
    logger.info("Using connection ID: %s", connection_id)

    with sender.FluentSender("speedtest", host=args.fluent_host, port=args.fluent_port) as fs:
        loop(fs, connection_id, args.interval)


if __name__ == "__main__":
    main()
