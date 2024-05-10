from utils.records_manager import exists, read_records, save_records, update_record


def add_new_records(episodes):
    records = read_records()
    for episode in episodes:
        if exists(records, episode):
            print(f"The episode {episode} already exits in the record.")
            continue
        update_record(records=records, name=episode, number=1)

    save_records(records=records)
