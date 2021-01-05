#from lib import todo_interface as td
from lib import todo_dict as td

# ls = ['take a walk', 'feed the dog', 'read books']


def main():
    prompt = td.Prompt()

    prompt.prompt_for_time_of_item()
    when = td.verify_time_of_item(prompt.when)

    item = prompt.prompt_for_value_of_item()
    td.update_todo(when, item)
    print(td.get_todo())


if __name__ == '__main__':
    main()

