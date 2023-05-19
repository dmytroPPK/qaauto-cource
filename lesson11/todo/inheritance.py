class Person:
    brain = True

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f'My name {self.first_name}'


person = Person('Joe', 'Coen')
print(person.first_name)
print(person.get_name())
print(person.brain)


class Student(Person):

    def __init__(self, first_name, last_name, graduate):
        super().__init__(first_name, last_name)
        self.graduate = graduate

    def get_graduate(self):
        return f'My graduate {self.graduate}'

    def get_name(self):
        return f'My name {self.first_name} in student class'


student = Student('Marte', 'Lee', 'Master')

print(student.get_graduate())
print(student.get_name())


# object

class Empoyee(Student):

    def __init__(self, first_name, last_name, graduate, salary):
        super().__init__(first_name, last_name, graduate)
        self.salary = salary

    def get_salary(self):
        return self.salary


employee = Empoyee('Mike', 'Bein', 'Master', 3000)


print('-------------------------')
print(employee.get_name())
print(employee.get_graduate())
print(employee.get_salary())

print(Empoyee.__mro__)