from lib import todo_dict as td


def standard_start_for_time():
    prompt = td.Prompt()

    # get unlimited prompting for items
    while prompt.prompt_to_continue() == 'y':
        when = prompt.prompt_for_time_of_item()
        item = prompt.prompt_for_value_of_item()

        td.update_time(when, item)

    return td.time


def update_items():
    pass


def main():
    items = standard_start_for_time()
    print(items)


if __name__ == '__main__':
    main()
