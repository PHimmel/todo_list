from lib import todo_dict as td


def standard_start_for_time(todo):
    prompt = td.Prompt()

    # get unlimited prompting for items
    while prompt.prompt_to_continue() == 'y':
        todo.when = prompt.prompt_for_time_of_item()
        todo.item = prompt.prompt_for_value_of_item()

        todo.update_time()
        #td.update_time(when, item)

    return todo # td.time


def update_items():
    pass


def main():
    todo = td.Todo()
    items = standard_start_for_time(todo)

    print(items.when, items.item, items.time)


if __name__ == '__main__':
    main()
