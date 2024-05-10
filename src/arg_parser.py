import argparse
import sys

from featrues import add_new_records
from utils.valitation import are_valid_episodes


APP_USAGE = """Application to track progress in learning polish with Piotr.

    python piotr.py <command> [<args>]

The available commands are:
    update   Update the episode(s).
    add      Add the new episode(s) to records.
    show     Show the current status of records
"""

FEAT_ADD_USAGE = """Add the new episode(s) to records.

    python piotr.py add [-h] episode [episode ...]

Episode should have format EXXX, where X is [0-9]. Example of usage:
    python piotr.py add E001
    python piotr.py add E001 E002
"""


class PiotrRecordManager(object):
    def __init__(self):
        parser = argparse.ArgumentParser(usage=APP_USAGE)
        parser.add_argument(
            "command", choices=["add", "update", "show"], help="command name"
        )
        parser.add_argument(
            "-v",
            "--version",
            help="show version and exit",
            action="version",
            version="1.0",
        )
        args = parser.parse_args(sys.argv[1:2])
        getattr(self, args.command)()

    def add(self):
        parser = argparse.ArgumentParser(usage=FEAT_ADD_USAGE)
        parser.add_argument(
            "episode",
            nargs="+",
            help="single episode (or list) to add to records (default number 1)",
        )

        args = parser.parse_args(sys.argv[2:])

        if not are_valid_episodes(args.episode):
            parser.error(
                f"Invalid episodes format: {args.episode}."
                " The episode should start with the letter 'E', followed by one or more digits."
            )

        add_new_records(args.episode)

    def show(self):
        print("not implemented yet")
        pass

    def update(self):
        print("not implemented yet")
        pass
