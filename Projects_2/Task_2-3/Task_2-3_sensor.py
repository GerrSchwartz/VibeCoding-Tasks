operator_name = input ('input operator name: ')
pressure_value = input ('input pressure value: ')

with open('C:/Users/Chernyx_Aleksandr/sensor.txt', 'w', encoding='utf-8') as file:
    file.write (f'input operator name: {operator_name}\ninput pressure value: {pressure_value}\ndata saved as sensor.txt')