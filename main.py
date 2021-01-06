from lib import todo_dict as td

# ls = ['take a walk', 'feed the dog', 'read books']


def standard_start():

    prompt = td.Prompt()

    while True:
        prompt.prompt_for_time_of_item()
        when = td.verify_time_of_item(prompt.when)

        item = prompt.prompt_for_value_of_item()
        td.update_todo(when, item)
        if prompt.prompt_to_continue() != 'y':
            break
    print(td.get_todo())


def main():
    standard_start()


if __name__ == '__main__':
    main()

