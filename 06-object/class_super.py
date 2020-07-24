class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

student = EmailPerson("Andy", "test123@gmail.com")
print(student.name)
print(student.email)