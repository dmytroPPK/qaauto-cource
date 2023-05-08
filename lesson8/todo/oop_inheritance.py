class Human:

    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f'Hi! My name is: {self.name}')


class Student(Human):

    def __init__(self, name, institution):
        super().__init__(name)
        self.institution = institution

    def who_am_i(self):
        super().who_am_i()
        print(f'I am a student of {self.institution}')


class Employee(Student):

    def __init__(self, name, institution, workplace):
        super().__init__(name, institution)
        self.workplace = workplace

    def who_am_i(self):
        super().who_am_i()
        print(f'I work in {self.workplace}')


class A:
    a = 1


class B:
    b = 2


class AB(A, B):
    pass


if __name__ == '__main__':
    human = Human('Mike')
    human.who_am_i()

    student = Student('John', 'Zhytomyr Politech')
    student.who_am_i()

    employee = Employee('Umerkumar', 'New Deli PTU', 'Google')
    employee.who_am_i()

    print(isinstance(human, Human))
    print(isinstance(student, Human))
    print(isinstance(employee, Human))

    print(issubclass(Student, Human))
    print(issubclass(Employee, Human))

    a_obj = A()
    print(a_obj.a)

    b_obj = B()
    print(b_obj.b)

    # Object ab_obj has a and b
    ab_obj = AB()
    print(ab_obj.a)
    print(ab_obj.b)

    print(AB.__mro__)
