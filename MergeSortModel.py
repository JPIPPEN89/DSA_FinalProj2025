import random
import time

from MergeSort import merge_sort

class MergeSortModel:

    def __init__(self):
        self.max_size = 1000000
        self.numbers = []

    def add_number(self, num):
        if len(self.numbers) < self.max_size:
            self.numbers.append(num)
        else:
            print("Limit Exceeded")

    def get_numbers(self):
        return self.numbers

    def sort(self):
        start_time = time.time()
        self.numbers = merge_sort(self.numbers)
        end_time = time.time()
        elapsed_time =end_time - start_time
        return elapsed_time