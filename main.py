import asyncio
from coorml_runner.entry import Entry
from coorml_runner.config import load_config
import logging
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.yaml')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    config = load_config(args.config)
    entry = Entry(api_endpoint=config['api_endpoint'], runner_name=config['name'])
    loop = asyncio.get_event_loop()
    loop.run_until_complete(entry.start())
