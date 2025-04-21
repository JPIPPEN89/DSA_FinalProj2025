import MergeSortModel
import random

class MergeSortController:

    def __init__(self):
        self.model = MergeSortModel()

    def load(self,count, low, high):
        for _ in range(count):
            self.model.add_number(random.randint(low, high))
        return count

    def sort(self):
        sort_time = self.model.sort()
        return sort_time

    def display(self):
        return self.model.get_numbers()