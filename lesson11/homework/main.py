from my_lib import Human, SmallHouse


if __name__ == '__main__':
    print(Human.default_info())
    person_mike = Human('Mike', 28)
    print(person_mike.info())
    small_house = SmallHouse(5500)
    person_mike.buy_house(small_house, 0)
    person_mike.earn_money()
    print(person_mike)
    person_mike.buy_house(small_house, 500)
    print(person_mike)
