medium_name = input('please input culture medium name: ').upper()
agar_concentration = input ('input agar concentration: ')
sterilisation_temperature = input('input sterilisation temperature: ')

with open('C:/Users/Chernyx_Aleksandr/recipe.txt', 'w', encoding='utf-8') as file:
    file.write (f'{medium_name}\n')
    file.write (f'agar concentration:\t{agar_concentration}\nsterilisation temperature:\t{sterilisation_temperature}')