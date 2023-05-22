# '''
# https://swapi.dev/
# Уважно вивчіть документацію цього API (https://swapi.dev/documentation) і напишіть програму, яка виводить на екран
# (і JSON-файл) інформацію про пілотів легендарного корабля Millennium Falcon.
#
# Інформація про корабель має містити такі пункти: назва, максимальна швидкість, клас, список пілотів.
# Усередині списку про кожен пілот має бути така інформація:
# ім'я,
# зріст,
# вага,
# рідна планета,
# посилання на інформацію про рідну планету.
# '''
import json
import requests
from pprint import pprint

class StarShipInfo:
    BASE_URL = "https://swapi.dev/api"
    END_POINT = "/starships/"
    SEARCH_PARAM = "?search={0}"
    SHOW_SFIELDS = ('name', 'max_atmosphering_speed', 'starship_class', 'crew', 'pilots')
    SHOW_PFIELDS = ('name', 'height', 'mass', 'homeworld')

    def __init__(self, name:str):
        self.__name = name
        self.__url = self.BASE_URL + self.END_POINT + self.SEARCH_PARAM.format(name)
        self.__ships = []


    @property
    def name(self):
        return self.__name

    @property
    def list_of_ships(self):
        return self.__ships


    def __make_request(self, url:str):
        return requests.get(url)

    def run(self):
        self.__get_ships(self.__url)
        self.__get_pilots()


    def __get_ships(self, url):
        res = self.__make_request(url)
        if res.json()['count'] == 0:
            raise ValueError("Wrong name of ship. No result to show")
        else:
            list_gener = (x for x in res.json()['results'])
            temp_list = []
            temp_dict = {}
            for item in list_gener:
                for k, v in item.items():
                    if k in self.SHOW_SFIELDS:
                        temp_dict[k] = v
                temp_list.append(temp_dict)
            self.__ships.extend(temp_list)
            del temp_list
            del temp_dict

    def __get_pilots(self):
        for ship in self.__ships:
            pilots_info = []
            for pilot in ship['pilots']:
                pilots_info.append(self.__get_pilot_info(pilot))
            ship['pilots'] = pilots_info

    def __get_pilot_info(self, url) -> dict:
        pilot = {}
        res = self.__make_request(url)
        if res.status_code != 200:
            raise ValueError('Wrong id of pilot. Bad request')
        else:
            for k, v in res.json().items():
                if k in self.SHOW_PFIELDS:
                    pilot[k] = v
        res_earth = self.__make_request(pilot['homeworld'])
        if res_earth.status_code != 200:
            raise ValueError('Wrong id of homeworld. Bad request')
        else:
            pilot['homeworld-name'] = res_earth.json()['name']

        return pilot




if __name__ == '__main__':
    app = StarShipInfo('Millennium Falcon')
    app.run()
    print(f"Search name of starship(s) - {app.name}")
    pprint(app.list_of_ships)
    print(f"\nResult in JSON format\n--> {json.dumps(app.list_of_ships)}")



