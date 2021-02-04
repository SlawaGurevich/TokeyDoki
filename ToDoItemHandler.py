from datetime import date, datetime, time
import pickle
import os

path_to_list = os.path.join(os.path.expanduser('~'), '.tokeydoki', 'items.db')

class ToDoItemHandler:
    to_do_items = []

    def __init__(self):
        self.load()

    def add_item(self, item):
        self.to_do_items.append(item)
        self.save()

    def remove_item(self, item):
        self.to_do_items.pop(self.to_do_items.index(item))
        self.save()

    def get_to_do_items(self):
        return self.to_do_items

    def load(self):
        if os.path.isfile(path_to_list):
            with open(path_to_list, 'rb') as file:
                self.to_do_items = pickle.load(file)
        else:
            if not os.path.isdir(os.path.dirname(path_to_list)):
                try:
                    os.makedirs(os.path.dirname(path_to_list))
                except OSError as e:
                    print(e)

            try:
                open(path_to_list, "w+").close()
            except OSError as e:
                print(e)

            self.to_do_items = []

    def save(self):
        with open(path_to_list, 'wb+') as file:
            pickle.dump(self.to_do_items, file)
