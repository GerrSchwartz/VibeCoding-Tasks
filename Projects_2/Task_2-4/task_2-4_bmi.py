height = float(input('input height '))/100
weight = float(input('input weight '))

bmi = weight / (height ** 2)
print(f'\n---BMI report---\nHeight:\t{height*100} cm\nWeight:\t{weight} kg\nBMI:\t{bmi:.2f}')