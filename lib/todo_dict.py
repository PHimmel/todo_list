"""
The basic structure is within a dict:
   { category , [item0, item1, item2, ... ]}
"""


class Todo:
    def __init__(self):
        self.time = self.create_time()
        self.day = self.create_week()
        self.when = None
        self.item = None

    @staticmethod
    def create_time():
        return {'morning': [],
                'afternoon': [],
                'evening': []}

    def create_week(self):
        return {'Monday': self.create_time(),
                'Tuesday': self.create_time(),
                'Wednesday': self.create_time(),
                'Thursday': self.create_time(),
                'Friday': self.create_time(),
                'Saturday': self.create_time(),
                'Sunday': self.create_time()}

    def update_time(self):
        self.time[self.when].append(self.item)


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
