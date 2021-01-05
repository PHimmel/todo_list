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

# Key value
def prompt_for_time_of_item():
    when = int(input('When is the item for:\n1) morning\n2) afternoon\n3) evening\n'))
    return when


# Value value
def prompt_for_value_of_item():
    item = str(input('What would you like to do then?\n'))
    return item


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
    when = prompt_for_time_of_item()
    when = verify_time_of_item(when)

    item = prompt_for_value_of_item()
    update_todo(when, item)
    print(get_todo())

# todo['morning'].append('go for a run')


if __name__ == '__main__':
    main()
