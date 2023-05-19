class Human:
    default_name = 'John'
    default_age = 18

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house: House = None

    def info(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"Name - {self.name}, Age - {self.age},\n" \
               f"House - {str(self.__house) if self.__house else 'No house'}, Money - {self.__money}$\n"

    @classmethod
    def default_info(cls) -> str:
        return f"default_name - {cls.default_name}, default_age - {cls.default_age}"

    def __make_deal(self, house: 'House', price):
        self.__money -= price
        self.__house = house

    def earn_money(self):
        self.__money += 5000

    def buy_house(self, house: 'House', discont):
        final_price = house.final_price(discont)
        if final_price > self.__money:
            print("Not enough money. Make money!")
        else:
            self.__make_deal(house, final_price)


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discont):
        return self._price - discont if self._price > discont else 0

    def __str__(self):
        return f"[Area-{self._area}|Price-{self._price}]"


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)
