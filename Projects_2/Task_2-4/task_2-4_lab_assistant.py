required_volume = int(input('input required volume in millilitres '))
required_mass = round(required_volume * 0.009, 2)
required_water_volume = required_volume

with open('C:/Users/Chernyx_Aleksandr/solution_recipe.txt', "w", encoding="utf-8") as file:
    file.write(f'Solution recipe\n--------------------\nFull volume:\t{required_volume} ml\nSalt mass:\t{required_mass} g\nWater volume:\t{required_water_volume} ml')