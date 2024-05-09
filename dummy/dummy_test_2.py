import json
import os

def read_records(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                records = json.load(file)
            except json.decoder.JSONDecodeError:
                records = {}
    else:
        records = {}
    return records

def save_records(records, filename):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def update_record(records, name, number):
    records[name] = number

if __name__ == "__main__":
    filename = 'records.json'
    records = read_records(filename)

    # Print current values of records
    print("Current records:")
    for name, number in records.items():
        print(f"{name}: {number}")

    # Modify the records (change or add new entries)
    update_record(records, "Alice", 123456789)
    update_record(records, "Bob", 987654321)

    # Save the updated records back to the file
    save_records(records, filename)

    print("Records updated and saved successfully.")
