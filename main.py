from lib import todo

# from lib import gui
# tkinter version not compatible with mac big sur os

def create_todo_list(ls):
    to_do = todo.Todo()
    [to_do.set_items(n) for n in ls]
    return to_do

def make_list():
    total = []
    while True:
        ls = input('What do you need to do?\n')
        if ls == '':
            break
        total.append(ls)
    return total

def what_has_been_done():
    pass

def what_to_add():
    pass

def main():
    # ls = ['take a walk', 'feed the dog', 'read books']
    ls = make_list() 
    to_do = create_todo_list(ls)
    print(to_do.get_items)

if __name__ == '__main__':
    main()

