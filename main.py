from lib import todo_dict as td


def standard_start_for_week(todo):
    prompt = td.Prompt()

    while prompt.prompt_to_continue() == 'y':
        todo.day = None
        todo.when = prompt.prompt_for_time_of_item()
        todo.item = prompt.prompt_for_value_of_item()

        todo.update_time()

    return todo


def standard_start_for_time(todo):
    prompt = td.Prompt()

    # get unlimited prompting for items
    while prompt.prompt_to_continue() == 'y':
        todo.when = prompt.prompt_for_time_of_item()
        todo.item = prompt.prompt_for_value_of_item()

        todo.update_time()

    return todo


def update_items():
    pass


def save_todo_to_file(todo):
    # determine best way to convert nested dict data into txt file and vice-versa
    with open('todo.txt', 'a') as doc:
        doc.write(todo.time['morning'][0])
        doc.close()


def main():
    todo = td.Todo()
    items = standard_start_for_time(todo)
    save_todo_to_file(todo)

    print(items.when, items.item, items.time)


if __name__ == '__main__':
    main()
