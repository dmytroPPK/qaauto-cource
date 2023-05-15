# any() -> []
# all() -> []

a = []
b = ''
c = ''
d = ''
#
# if any([a, b, c, d]):
#     print("True")
# else:
#     print('False')

print(any([True for i in range(1000000000) if i == 1000]))