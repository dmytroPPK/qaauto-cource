# john = {
#     "name": "Joe",
#     "age": 23,
#     "salary": 20000
# }
#
# Mark = {
#     "name": "Mark",
#     "age": 25,
#     "salary": 22000
# }
#
#
# def get_name(person: dict) -> str:
#     return person["name"]
#
#
# def update_salary(person: dict) -> int:
#     return person["salary"] * 0.1
from random import randint

LOCAL_VAR = 'Python'

class People:

    country = 'Ukraine'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def my_name_is(self) -> str:
        return f"My name {self.name}"

    def my_age(self) -> str:
        return f"My age {self.age}"

    def language(self) -> str:
        return f"My language {LOCAL_VAR}"

vadym: People = People('Vadym', 20)
print(type(vadym))
#
# print(vadym.my_name_is())
# print(vadym.language())


class DataGeneration:

    @staticmethod
    def generation_name(name):
        new_name = f'{name} {randint(1, 50000)}'
        return new_name



data_generator = DataGeneration()
print(data_generator.generation_name('Joe'))

print(DataGeneration.generation_name('Marta'))


def get_age_from_class(my_class: People):
    print(my_class.my_name_is())

get_age_from_class(vadym)