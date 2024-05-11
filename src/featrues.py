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


def show_records(args):
    records = read_records()

    if args.sort:
        records = sort(records, args.sort)

    if args.bottom:
        records = dict(list(records.items())[-args.bottom :])
    elif args.top:
        records = dict(list(records.items())[: args.top])

    print_records(records)


def pick_sort_option(sort_option):
    if "-" in sort_option:
        return sort_option.split("-")
    elif sort_option in ("ep", "num"):
        return [sort_option, "asc"]
    else:
        return ["num", sort_option]


def print_records(records):
    for episode, value in records.items():
        print(f"{episode}: {value}")


def sort(records, sort_option):
    what, how = pick_sort_option(sort_option)
    param = 1 if what == "num" else 0
    sorted_records = sorted(
        records.items(), key=lambda x: x[param], reverse=(how == "desc")
    )
    return dict(sorted_records)
