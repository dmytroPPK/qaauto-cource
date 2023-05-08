class PhoneNumber:

    def __init__(self, number):
        self.number = number

    def format_to_ukraine(self):
        return f'+38{self.number}'


class User:
    prefix = 'Sir '

    def __init__(self, name, surname, number):
        """

        :param name: user's name
        :param surname:
        """

        self.one = 1  # explain
        self.name = name
        self.surname = surname
        self.phone_number = PhoneNumber(number)
        self.sir_name = self.prefix + name

    def get_whole_name(self):
        return f'{self.name} {self.surname}'

    @staticmethod
    def new_method():
        return 1 + 1

    @staticmethod
    def strip(msg: str):
        return msg.strip()

    def mod_name(self):
        name = self.get_whole_name()
        name = 'Sir ' + name
        self.sir_name = name

    def show_all(self):
        full_name = self.get_whole_name()
        phone = self.phone_number.format_to_ukraine()
        return f'My name is: {full_name}.\nMy phone number is: {phone}'


class Developer(User):

    def __init__(self, name, surname, number, position):
        super().__init__(name, surname, number)
        self.position = position

    def do_some_bug_in_code(self):
        print('Working on new bug!')

    def show_all(self):
        full_name = self.get_whole_name()
        return f"My name is: {full_name}. I'm {self.position}!"


class QA(User):

    def find_some_bug(self):
        print('Finding some bug!')


user_1 = User('John', 'Snow', 123456789)
print(user_1.show_all())
dev1 = Developer('Jonny', 'Mnemonic', 123456789, 'Senior Developer')
dev1.do_some_bug_in_code()
print(dev1.show_all())
print(dev1.phone_number.number)
dev1.phone_number.number = 1
print(dev1.phone_number.number)
