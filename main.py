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

    # todo = td.TodoInterface()
    #
    # todo.create_list_from_user_input()
    # # t  o_do = todo.create_todo_list(ls)
    # #todo.todo.remove_items('df')
    # print(f'{todo.get_items()} are your items')


if __name__ == '__main__':
    main()

