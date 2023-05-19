class Student:

    def __init__(self, first_name, last_name, graduate):
        self.first_name = first_name   # public
        self._last_name = last_name    # protect
        self.__graduate = graduate     # private

    def get_graduate(self):
        return self.__graduate

    def _get_first_name(self):
        return self.first_name

    def __get_last_name(self):
        return self._last_name


student = Student('Joe', 'Coin', 'Master')

print(student.first_name)
print(student._last_name)
print(student._Student__graduate)

print(student.__dict__)

print(student.get_graduate())
print(student._get_first_name())
print(student._Student__get_last_name())