import SLL as SLL
from Student import Student
import pandas as pd

class LinkedListController:
    def __init__(self):
        self.sll = SLL.SLL()

    def append(self, firstName, lastName, SSN, phone, email):
        student = Student(firstName,lastName, SSN, phone, email)
        self.sll.append(student)

    def prepend(self, firstName, lastName, SSN, phone, email):
        student = Student(firstName,lastName, SSN, phone, email)
        self.sll.prepend(student)

    def display(self):
        return str(self.sll)

    def load(self, fileName):
        df = pd.read_csv(fileName)
        for index, row in df.iterrows():
            student = Student(row['first_name'], row['last_name'], row['ssn'], row['phone'], row['email'])
            self.sll.insert_in_order(student)
        return len(df)

    def delete(self, deleteSSN):
        student = Student(first_name="", last_name="", ssn=deleteSSN, phone="", email="")
        self.SLL.delete(student)