from lib import todo_dict as td

# ls = ['take a walk', 'feed the dog', 'read books']


def standard_start():

    prompt = td.Prompt()

    # get unlimited prompting for items
    while prompt.prompt_to_continue() == 'y':
        when = prompt.prompt_for_time_of_item()
        item = prompt.prompt_for_value_of_item()

        td.update_todo(when, item)

    return td.todo


def main():
    items = standard_start()
    print(items)


if __name__ == '__main__':
    main()

