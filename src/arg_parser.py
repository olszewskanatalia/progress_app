import argparse
import sys

from featrues import add_new_records, update_records, show_records
from utils.valitation import are_valid_episodes


APP_USAGE = """Application to track progress in learning polish with Piotr.

    python piotr.py <command> [<args>]

The available commands are:
    add      Add the new episode(s) to the records.
    show     Show the current status of the records.
    update   Update the episode(s) values.
"""

FEAT_ADD_USAGE = """Add the new episode(s) to the records.

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

FEAT_SHOW_USAGE = """Show the current status of the records..

    python piotr.py show [-h] [-a | -t N | -b N] [-s [WHAT | HOW | WHAT-HOW]]

Without any paramenters the program will show all the values without sorting.
For [-t | -b] N should have a positive integer value.
Possible parameters for sorting are:
    - ep        - sort by episode name (default asc)
    - num       - sort by number (default asc)
    - asc       - sort ascending (default by numer)
    - desc      - sort descending (default by numer)
    - ep-asc    - sort ascending by episode name
    - ep-desc   - sort decending by episode name
    - num-asc   - sort ascending by number
    - num-desc  - sort descending by number
Default sort is ascending by number.

Example of usage:
    python piotr.py show
    python piotr.py show -a
    python piotr.py show -t 5
    python piotr.py show -b 10
    python piotr.py show -a -s ep
    python piotr.py show -t 5 -s num
    python piotr.py show -b 1 -s asc
    python piotr.py show -s ep-desc
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
        parser = argparse.ArgumentParser(usage=FEAT_SHOW_USAGE)
        show_group = parser.add_mutually_exclusive_group()
        show_group.add_argument(
            "-a", "--all", action="store_true", help="show all records"
        )
        show_group.add_argument(
            "-t",
            "--top",
            metavar="N",
            type=self._check_non_negative,
            help="show top N records",
        )
        show_group.add_argument(
            "-b",
            "--bottom",
            metavar="N",
            type=self._check_non_negative,
            help="show bottom N records",
        )
        parser.add_argument(
            "-s",
            "--sort",
            nargs="?",
            metavar=("WHAT | HOW | WHAT-HOW"),
            help="sort displayed records",
            choices=[
                "num",
                "ep",
                "asc",
                "desc",
                "num-asc",
                "num-desc",
                "ep-asc",
                "ep-desc",
            ],
            const="num-asc",
        )

        args = parser.parse_args(sys.argv[2:])

        show_records(args)

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

    def _check_non_negative(self, value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        return ivalue
