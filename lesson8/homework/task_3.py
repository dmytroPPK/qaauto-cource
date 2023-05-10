# 3. Написать три класса:
#
# 3.1 класс Справочник(Записная книга, Телефонная книга), описывающий взаимодействие с телефонным справочником.
# Объект этого класса аггрегирует в себе объекты другого класса - Запись(множество записей)
#
# 3.2 класс Запись(Абонент), хранящий такие данные: Имя, Фамилия(необязательно), Телефон, Дата рождения(необязательно).
# Обеспечить валидацию данных и запрет на изменение этих данных другим классом
#
# 3.3 класс Интерфейс, которые обеспечивает взаимодействие с пользователем, который вводит данные в терминал.
# Обеспечить защиту от неверного ввода
#
# 3.4 В функции __main__() написать точку входа и выхода их программы(для ввода пользователя).
#
# Данная программа должна обеспечить: добавление, удаление, редактирование записей с терминала. По умолчание в
# справочнике есть номера экстренных служб, которые нельзя удалить или изменить(ни юзеру, ни другому программисту).
from re import match
from datetime import datetime


class Interface:
    def __init__(self):
        self.__book = PhoneBook()

    def run(self):
        while True:
            try:
                print("\n" + "Welcome to PhoneBook ".center(35, '-'))
                print('Enter "1" to get all records,'
                      ' "2" to add record,'
                      ' "3" to delete record,\n'
                      '\t  "4" to search by word,'
                      ' "5" to update record.\n'
                      'Type Q to exit ...')
                user_input = input('Your choise: ')
                if user_input == '1':
                    self.show_records()
                elif user_input == '2':
                    self.add_record()
                elif user_input == '3':
                    self.delete_record()
                elif user_input == '4':
                    self.search()
                elif user_input == '5':
                    self.udate_record()
                elif user_input.lower() == 'q':
                    print("Program is exited. Bye.")
                    break
                else:
                    print("Invalid choice, please try again. Press any key to continue ", end='')
                    input()

            except IndexError as ie:
                print(f'\tError: {ie}')
            except ValueError as ve:
                print(f'\tError: {ve}')
            except Exception as ex:
                print("\nInternal error was occured ...")
                print(ex)
                exit()

    def show_records(self):
        records: ['Record'] = self.__book.get_records()
        sign = '(S)'
        for i, v in enumerate(records):
            sign = sign if v.protected else ''
            print(f'\t{i + 1}) {str(v)}{sign}')

    def _get_record_byid(self, record_id: int) -> 'Record':
        return self.__book.get_records()[record_id]

    def add_record(self):
        name = input('\tType name: ').strip()
        phone = input('\tType phone in format 066-154-54-54: ').strip()
        surname = input('\tType surname: ').strip()
        birthday = input('\tType birthday in format - 2000-12-31: ').strip()
        new_record = Record(name, phone, surname, birthday)
        self.__book.add_record(new_record)
        print(f'\tRecord [{str(new_record)}] was added')

    def udate_record(self):
        try:
            print('\t... Be considerate, service records cannot be updated')
            index_to_update = int(input("\tEnter id of record to update: ").strip())
            old_record: 'Record' = self._get_record_byid(index_to_update - 1)
            name = input(f'\tType name [{old_record.name}]: ').strip()
            phone = input(f'\tType phone in format 066-154-54-54 [{old_record.phone}]: ').strip()
            surname = input(f'\tType surname [{old_record.surname}]: ').strip()
            birthday = input(f'\tType birthday in format 2000-12-31 [{old_record.birthday}]: ').strip()

            name = name if name else old_record.name
            phone = phone if phone else old_record.phone
            surname = surname if surname else old_record.surname
            birthday = birthday if birthday else old_record.birthday
            new_record = Record(name, phone, surname, birthday)

            is_updated = self.__book.update_record(index_to_update - 1, new_record)
            if not is_updated:
                print("\tError: Not allowed to update service records")
            else:
                print(f'\tRecord was updated')
        except ValueError as ex:
            raise ValueError("It is not an integer value" + str(ex))

    def delete_record(self):
        try:
            index_to_delete = int(input("\tEnter id of record to delete: ").strip())
            is_deleted = self.__book.del_record(index_to_delete - 1)
            if not is_deleted:
                print("\tError: Not allowed to delete service records")
            else:
                print(f'\tRecord with id - {index_to_delete} was deleted')
        except ValueError:
            raise ValueError("It is not an integer value")

    def search(self):
        search_word = input("Enter search word: ")
        result = self.__book.search_records(search_word)
        if not result:
            print('\tNothing to show.')
        else:
            for i, v in enumerate(result):
                print(f"\t{i + 1}) {str(v)}")


class PhoneBook:
    def __init__(self):
        self.__records: ['Record'] = []
        self.__add_services()

    def __add_services(self):
        services_list = [
            Record('Service-1', '066-111-10-10', protected=True),
            Record('Service-2', '066-222-10-10', protected=True),
            Record('Service-3', '066-333-10-10', protected=True),
            Record('Service-4', '066-444-10-10', protected=True)
        ]
        self.__records += services_list

    def __is_protected(self, id_record) -> bool:
        if id_record >= len(self.__records):
            raise IndexError("Index error of records' list")
        if not self.__records[id_record].protected:
            return False
        return True

    def get_records(self) -> ['Record']:
        return self.__records

    def add_record(self, record: 'Record'):
        self.__records.append(record)

    def del_record(self, id_record: int) -> bool:
        if self.__is_protected(id_record):
            return False
        del self.__records[id_record]
        return True

    def update_record(self, id_record: int, new_record: 'Record') -> bool:
        if self.__is_protected(id_record):
            return False
        self.__records[id_record] = new_record
        return True

    def search_records(self, phraze: str) -> ['Record']:
        list_ids = []

        for i, v in enumerate(self.__records):
            if phraze.lower() not in repr(v):
                continue
            list_ids.append(i)
        list_result = [self.__records[i] for i in list_ids]
        return list_result


class Record:
    def __init__(self, name: str, phone: str, surname: str = '', birthday: str = '', protected: bool = False):

        self._validator(name, phone, surname, birthday, protected)
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        self.__birthday = birthday
        self.__protected = protected

    @classmethod
    def _phone_is_valid(cls, phone: str) -> bool:
        pattern = r"\d{3}-\d{3}-\d{2}-\d{2}"
        if match(pattern, phone):
            return True
        return False

    @classmethod
    def _birthday_is_valid(cls, birthday: str) -> bool:
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @classmethod
    def _validator(cls, name, phone, surname, birthday, protected):
        if not name or not phone:
            raise ValueError('name and phone are required')
        if not isinstance(name, str):
            raise ValueError('name must be string type')
        if not isinstance(surname, str):
            raise ValueError('surname must be string type')
        if not cls._phone_is_valid(phone):
            raise ValueError('Invalid phone format')
        if birthday != '' and not cls._birthday_is_valid(birthday):
            raise ValueError('Invalid birthday format')
        if not isinstance(protected, bool):
            raise ValueError("protected field must be bool type")

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def phone(self):
        return self.__phone

    @property
    def birthday(self):
        return self.__birthday

    @property
    def protected(self):
        return self.__protected

    def __str__(self):
        return f"{self.__name} {self.__phone} {self.__surname} {self.__birthday}"

    def __repr__(self):
        str_for_search = f"{self.__name}{self.__surname}{self.__phone}{self.__birthday}"
        return str_for_search.lower()


if __name__ == '__main__':
    app = Interface()
    app.run()
