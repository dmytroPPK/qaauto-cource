#4. С помощью фреймворка unittests, покрыть тестами два класса(Справочник и Запись),
# которые подтверждают работу методов этих классов.

import unittest
from task_3 import Record, PhoneBook

# implemented a few tests

class RecordTest(unittest.TestCase):

    valid_phone = '111-000-55-55'
    invalid_phone = '8787-fd-fdfd-dfd'

    def test_valid_phone(self):
        self.assertTrue(Record._phone_is_valid(self.valid_phone))
    def test_invalid_phone(self):
        self.assertFalse(Record._phone_is_valid(self.invalid_phone))


class PhoneBookTest(unittest.TestCase):

    phone_book = None
    record = None
    service_record = None

    @classmethod
    def setUpClass(cls):
        cls.record = Record('John', '111-111-00-00')
        cls.service_record = Record('SuperService','055-123-23-23', protected=True)
        cls.phone_book = PhoneBook()

    def test_add_new_record(self):
        self.phone_book.add_record(self.record)
        added_record = self.phone_book.get_records()[-1]
        self.assertTrue(str(self.record) == str(added_record))

    def test_cannot_delete_service_record(self):
        self.phone_book.add_record(self.service_record)
        result = self.phone_book.del_record(-1)
        self.assertFalse(result)

    @classmethod
    def tearDownClass(cls):
        cls.phone_book = None
        cls.record = None
        cls.service_record = None


if __name__ == '__main__':
    unittest.main()
