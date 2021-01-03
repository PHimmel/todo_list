from lib import todo

# from lib import gui
# tkinter version not compatible with mac big sur os


class TodoInterface:

    def __init__(self):
        self.todo = todo.Todo()

    def create_todo_list(self, ls):
        # to_do = todo.Todo()
        [self.todo.set_items(n) for n in ls]
        # return to_do

    def make_list(self):
        total = []
        while True:
            ls = input('What do you need to do? Key `Enter` when done.\n')
            if ls == '':
                break
            total.append(ls)
        return total

    def what_has_been_done(self):
        pass

    def what_to_add(self):
        pass

