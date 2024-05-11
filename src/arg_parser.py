import argparse
import sys

from featrues import add_new_records, update_records
from utils.valitation import are_valid_episodes


APP_USAGE = """Application to track progress in learning polish with Piotr.

    python piotr.py <command> [<args>]

The available commands are:
    add      Add the new episode(s) to records.
    show     Show the current status of records
    update   Update the episode(s).
"""

FEAT_ADD_USAGE = """Add the new episode(s) to records.

    python piotr.py add [-h] episode [episode ...]

The episode should start with the letter `E`, followed by one or more digits.
Example of usage:
    python piotr.py add E001
    python piotr.py add E001 E002
"""

FEAT_UPDATE_USAGE = """Update the episode(s).

    python piotr.py update [-h] [-n NUMBER | -s SET_UP | -r] episode [episode ...]

The episode should start with the letter `E`, followed by one or more digits.
Example of usage:
    python piotr.py update E001
    python piotr.py update E001 E002 -n 2
    python piotr.py update E001 -s 76
    python piotr.py update E001 E002 E003 -r

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
        parser = argparse.ArgumentParser(usage=FEAT_UPDATE_USAGE)
        parser.add_argument(
            "episode",
            nargs="+",
            help="single episode (or list) to update (default updated by 1)",
        )
        update_group = parser.add_mutually_exclusive_group()
        update_group.add_argument(
            "-n", "--number", type=int, help="update episodes by N number"
        )
        update_group.add_argument("-s", "--set-up", type=int, help="set records to N")
        update_group.add_argument(
            "-r",
            "--reset",
            action="store_true",
            help="reset progress on episodes. These records will be set to 0",
        )

        args = parser.parse_args(sys.argv[2:])

        if not are_valid_episodes(args.episode):
            parser.error(
                f"Invalid episodes format: {args.episode}."
                " The episode should start with the letter 'E', followed by one or more digits."
            )

        update_records(args)
