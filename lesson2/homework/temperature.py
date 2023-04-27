# перетворення з С в F -> T (° F) = T (° C) × 1,8 + 32
# перетворення з С в K -> K = °C + 273.15

user_input = input("Please, type temperature in celsius ...\n-> ")
temp_c = int(user_input)
temp_f = temp_c * 1.8 + 32
temp_k = temp_c + 273.15

degree_sign = u'\xb0'
output = f'''Result:
 {temp_c}{degree_sign}C = {temp_f}{degree_sign}F
 {temp_c}{degree_sign}C = {temp_k}{degree_sign}K
'''
print(output)
