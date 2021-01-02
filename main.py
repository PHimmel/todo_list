from todo import *

def create_list(ls):
    todo = Todo()
    [todo.set_items(n) for n in ls]
    return todo

def main():
    ls = ['take a walk', 'feed the dog', 'read books']
    todo = create_list(ls)
    print(todo.get_items)

if __name__ == '__main__':
    main()

