# Dict

my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True, 'city': 'Dnipro'}
my_dict_2 = {'city': 'Kyiv', 'country': 'Ukraine'}

print(len(my_dict))

print(my_dict['books'])

print(my_dict.get('books', '+'))

print(list(my_dict.values()))
print(tuple(my_dict.keys()))

my_dict_new = my_dict | my_dict_2
my_dict |= my_dict_2
#
# print(my_dict_new)
# print(my_dict)


# new_dict = my_dict.update(my_dict_2)
# print(my_dict)
#
# print(list(my_dict.items()))
#
# print(my_dict.pop('city'))


# last_value_in_dict = my_dict.popitem()
# print(last_value_in_dict * 3)
#
# last_value_in_dict_ = my_dict.pop('name')
# print(last_value_in_dict_ * 3)

# print(my_dict)

# ---------------------------

# my_dict['zip_code'] = '02225'
#
# print(my_dict)
# del my_dict['zip_code']
# print(my_dict)
#
# print('age' in my_dict)


# Set   {}

# empty_set = set()
#
# print(type(empty_set))
#
# my_list = [1, 23, 32, 32, 43, 1, 2, 3, 4, 2, 1, 32]
#
# print(set('my_set_my_se'))
#
# my_set = set(my_list)
#
# print(my_set)
#
# my_set_2 = my_set.add(222)
# print(list(my_set).sort())
#
# #frozenset()
#
# my_frozenset = frozenset()
# print(type(my_frozenset))
# # ---------------------------------------------------
#
# count = 1
#
# while count <= 5:
#     print(count)
#     count += 1
#     if count == 2:
#         name = input('Set name : ')
#         print(f'Count {count}')
#     else:
#         if name == 'Joe':
#             print(f'My name is {name}')
#             break
#         print('*************')
#     if name == 'John':
#         print('Continue.....')
#         continue
#     print('*************')
#     print('*************')
#
# print('Finish')

# ages = [12, 22, 31, 44, 52]
age_2 = [122, 212, 31, 434, 352]
age_3 = [122, 212, 31, 434, 352]

# print(type(enumerate([],1)))

# for value, index in enumerate(ages):
#     print(f'My value is {value} and index {index}')
#     if value == 31:
#         print(f"Finish. Index {index}")

# for i, j, z in zip(ages, age_2, age_3):
#     print(f'First list value {i}, second list value {j} and z: {z}')
#     if i == j:
#         print('Finish')
#         break
#
# print('Good')

my_list = []
for i in range(8):
    my_list.append(i ** 2)
print(my_list)

my_list_new = [x ** 2 for x in range(8) if x % 2 == 0]

print(my_list_new)
print(my_list == my_list_new)

a = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print(a)

names = ['Joe', 'Lisa', 'Kate', 'Mike']
ages = [122, 212, 31, 434, 352]

my_dict = {name: age for name, age in zip(names, ages)}

print(my_dict)

new_dict_2 = dict(zip(names, ages))
print(new_dict_2)
