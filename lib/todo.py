class Todo:
    def __init__(self, items=None):
        if items == None:
            items = []
        self.items = items
    
    def __repr__(self):
        return f'Todo(): {self.items}'

    def get_items(self):
        return self.items

    def set_items(self, item):
        self.items.append(item)

    def remove_items(self, item):
        self.items.remove(item)

