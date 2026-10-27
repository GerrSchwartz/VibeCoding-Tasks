proteins_mass = float(input('input protein mass '))
fats_mass = float(input('input fats mass '))
carbohydrates_mass = float(input ('input carbohydrates mass '))

calories = proteins_mass*4 + fats_mass*9 + carbohydrates_mass*4
print(f'this product has {calories} calories')