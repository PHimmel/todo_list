"""
The basic structure is within a dict:
   { category , [item0, item1, item2, ... ]}
"""

todo = {'morning': [],
        'afternoon': [],
        'evening': []}


class Todo:
    def __init__(self):
        self.items = {}


class Prompt:
    def __init__(self):
        self.when = None
        self.what = None

    # Key value
    def prompt_for_time_of_item(self):
        self.when = int(input('When is the item for:\n1) morning\n2) afternoon\n3) evening\n'))
        return self.when

    # Value value
    def prompt_for_value_of_item(self):
        self.what = str(input('What would you like to do then?\n'))
        return self.what

    @staticmethod
    def prompt_to_continue():
        go_on = input('Enter \'y\' to add more:\n')
        return go_on


def verify_time_of_item(when):
    if when > 3 or when < 0:
        raise ValueError('Only use integers from 1 - 3\n')
    if when == 1:
        return 'morning'
    elif when == 2:
        return 'afternoon'
    else:
        return 'evening'


def update_todo(when, item):
    todo[when].append(item)


def get_todo():
    return todo


def main():
    prompt = Prompt()

    when = prompt.prompt_for_time_of_item()
    when = verify_time_of_item(when)

    item = prompt.prompt_for_value_of_item()
    update_todo(when, item)
    print(get_todo())

# todo['morning'].append('go for a run')


if __name__ == '__main__':
    main()
