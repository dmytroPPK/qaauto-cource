from abc import ABC, abstractmethod


class People(ABC):

    def __init__(self, first_name, last_name):
        self.first_name = first_name   # public
        self._last_name = last_name    # protect

    def get_first_name(self):
        return self.first_name

    @abstractmethod
    def get_last_name(self):
        pass


class Student(People):

    def __init__(self, first_name, last_name, graduate):
        super().__init__(first_name, last_name)
        self.__graduate = graduate  # private

    def get_graduate(self):
        return self.__graduate

    # def get_last_name(self):
    #     return f'{self._last_name} '


student = Student('Joe', 'Coin', 'Master')
print(student.first_name)