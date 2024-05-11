from utils.records_manager import exists, read_records, save_records, update_record


def add_new_records(episodes):
    records = read_records()

    for episode in episodes:
        if exists(records, episode):
            print(f"The episode {episode} already exits in the record.")
            continue

        update_record(records=records, name=episode, number=1)
    save_records(records)


def update_records(args):
    records = read_records()

    for episode in args.episode:
        if not exists(records, episode):
            print(f"The episode {episode} does not exit in the record.")
            continue

        update_to = None

        if args.reset:
            update_to = 0
        elif args.set_up:
            update_to = args.set_up
        elif args.number:
            update_to = records.get(episode, 0) + args.number
        else:
            update_to = records.get(episode, 0) + 1

        update_record(records=records, name=episode, number=update_to)
    save_records(records)
