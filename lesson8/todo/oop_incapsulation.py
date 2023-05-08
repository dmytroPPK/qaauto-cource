class Employee:

    __employee_id = 0

    def __init__(self, name, position, phone, birth_date):
        self.name = name
        self.position = position
        self._phone = phone
        self.__birth_date = birth_date

    def set_phone(self, new_phone: str):
        if new_phone.isdigit():
            self._phone = new_phone

    def get_phone(self):
        return f'+38{self._phone}'

    def get_birth_date(self):
        return self.__birth_date


class QA(Employee):

    def __init__(self, name, phone, birth_date):
        super().__init__(name, 'QA', phone, birth_date)

    def get_employee_id_as_qa(self):
        return self.__employee_id


if __name__ == '__main__':
    employee = Employee('John', 'QA', '123456789', '01.01.2000')
    print(employee.name)
    print(employee.position)
    print(employee._phone)

    try:
        print(employee.__birth_date)
    except AttributeError:
        print('You have no access to private attribute')

    print(employee.get_phone())
    print(employee.get_birth_date())

    employee_qa = QA('Tom', '221133444', '11.11.2000')

    try:
        print(employee_qa.get_employee_id_as_qa())
    except AttributeError:
        print('Child object has no access to parent private attribute')
