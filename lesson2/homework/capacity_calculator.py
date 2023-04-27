# температура суміші = (v1*t1 + v2*t2) / (v1 + v2)

print('...Capacity calculator...')
print('Part 1 of water:')
temp_1 = int(input(" Temperature_1 = "))
capacity_1 = int(input(" Capacity_1 = "))
print('Part 2 of water')
temp_2 = int(input(" Temperature_2 = "))
capacity_2 = int(input(" Capacity_2 = "))

capacity_result = capacity_1 + capacity_2
temp_result = (temp_1 * capacity_1 + temp_2 * capacity_2) / (capacity_result)

degree_sign = u'\xb0'
output = f'''Result:
 Capacity = {capacity_result} liters
 Temperature of capacity = {temp_result:.2f}{degree_sign}C'''

print(output)
