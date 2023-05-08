class Employee:

    def __init__(self, name, position, phone, birth_date):
        self.name = name
        self.position = position
        self.phone = phone
        self.birth_date = birth_date

    def __setattr__(self, key, value):
        if not hasattr(self, 'birth_date') and key == 'birth_date' or key != 'birth_date':
            super().__setattr__(key, value)
        else:
            raise AttributeError('You cannot change the age')

    def get_name(self):
        return self.name

    def __len__(self):
        return len([self.name, self.position, self.phone, self.birth_date])

    def __repr__(self):
        return f'Employee. Name: {self.name}. Position: {self.position}'

    def __str__(self):
        return f'Employee. Name: {self.name}. Position: {self.position}. Birth date: {self.birth_date}'

    def __del__(self):
        print(f'Object of {self.__class__.__name__} has finished job and clean up memory')
        del self.name
        del self.position
        del self.phone
        del self.birth_date


if __name__ == '__main__':
    employee = Employee('John', 'QA', '123456789', '01.01.2000')

    try:
        employee.birth_date = '12.12.12'
    except AttributeError as e:
        print(e)

    print(employee)
    print(str(employee))
    print(len(employee))
