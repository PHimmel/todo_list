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
#
