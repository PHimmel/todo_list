from lib import todo_interface as td

# ls = ['take a walk', 'feed the dog', 'read books']


def main():
    todo = td.TodoInterface()

    ls = todo.make_list()
    to_do = todo.create_todo_list(ls)

    print(f'{to_do.get_items} are your items')


if __name__ == '__main__':
    main()

