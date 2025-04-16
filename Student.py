
class Student:

    def __init__(self, first_name, last_name, ssn, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"\n\nStudent Information:\nName: {self.first_name} {self.last_name}\nSSN: " \
               f"{self.ssn}\nPhone: {self.phone}\nEmail: {self.email}"

    def __eq__(self, other):
        #return self.ssn == other.ssn
        if isinstance(other, Student):
            return self.ssn == other.ssn
        if isinstance(other, int):
            return self.ssn == other

    def __ge__(self, other):
        return self.ssn >= other.ssn

    def __lt__(self, other):
        return self.ssn < other.ssn

    def getName(self):
        return self.last_name + ", " + self.first_name

    def getPhone(self):
        return self.phone

    def __hash__(self):
        h = 0
        for char in str(self.ssn):
            h+= ord(char)
        return h
