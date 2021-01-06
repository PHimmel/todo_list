"""
The basic structure is within a dict:
   { category , [item0, item1, item2, ... ]}
"""

todo = {'morning': [],
        'afternoon': [],
        'evening': []}


def update_todo(when, item):
    todo[when].append(item)

# class Todo:
#     def __init__(self):
#         self.items = {}


# class Todo:
#     def __init__(self, items=None):
#         if items is None:
#             items = []
#         self.items = items
#
#     def __str__(self):
#         return self.__repr__()
#
#     def __repr__(self):
#         return f'Todo(): {self.items}'
#
#     def get_items(self):
#         return f'{self.items} are your items'
#
#     def set_items(self, item):
#         self.items.append(item)
#
#     def remove_items(self, item):
#         self.items.remove(item)


class Prompt:
    def __init__(self):
        self.when = None
        self.what = None

    # Key value
    def prompt_for_time_of_item(self):
        self.when = int(input('When is the item for:\n1) morning\n2) afternoon\n3) evening\n'))
        return self.verify_time_of_item()

    # Value value
    def prompt_for_value_of_item(self):
        self.what = str(input('What would you like to do then?\n'))
        return self.what

    @staticmethod
    def prompt_to_continue():
        go_on = input('Enter \'y\' to add items to do:\n')
        return go_on

    def verify_time_of_item(self):
        if self.when > 3 or self.when < 0:
            raise ValueError('Only use integers from 1 - 3\n')
        if self.when == 1:
            return 'morning'
        elif self.when == 2:
            return 'afternoon'
        else:
            return 'evening'
