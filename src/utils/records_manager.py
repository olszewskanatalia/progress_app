import json
import os


FILENAME = "records.json"


def read_records(filename=FILENAME) -> dict[str, int]:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                records = json.load(file)
            except json.decoder.JSONDecodeError:
                records = {}
    else:
        records = {}
    return records


def save_records(records, filename=FILENAME) -> None:
    with open(filename, "w") as file:
        json.dump(records, file, indent=4)


def update_record(records, name, number):
    records[name] = number


def exists(records, name) -> bool:
    if name in records.keys():
        return True
    return False
