from lib import todo_interface as td

# ls = ['take a walk', 'feed the dog', 'read books']


def main():
    todo = td.TodoInterface()

    todo.create_list_from_user_input()
    # t  o_do = todo.create_todo_list(ls)
    #todo.todo.remove_items('df')
    print(f'{todo.get_items()} are your items')


if __name__ == '__main__':
    main()

