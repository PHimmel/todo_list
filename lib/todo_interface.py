from lib import todo

# from lib import gui
# tkinter version not compatible with mac big sur os


class TodoInterface:

    def __init__(self):
        self.todo = todo.Todo()
       # self.list = []

    def get_items(self):
        return self.todo.get_items()

    def set_items(self, item):
        self.set_items(item)

    # def create_todo_list_from_list(self, ls):
    #     [self.todo.set_items(n) for n in ls]

    def create_list_from_user_input(self):
        while True:
            ls = input('What do you need to do? Key `Enter` when done.\n')
            if ls == '':
                break
            #self.list.append(ls)
            self.todo.set_items(ls)

    def what_has_been_done(self):
        pass

    def what_to_add(self):
        pass

