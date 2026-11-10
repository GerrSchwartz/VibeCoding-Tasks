donor_blood = input('input donor blood group ').upper()
patient_blood = input('input patient blood type').upper()

if patient_blood == 'I':
    if donor_blood == 'I': print('blood matches')
    else: print('blood mismatch')

elif patient_blood == 'II':
    if donor_blood == 'I' or donor_blood == 'II': print('blood matches')
    else: print("blood mismatch")

elif patient_blood == 'III':
    if donor_blood == 'I' or donor_blood == 'III': print('blood matches')
    else: print('blood mismatch')

elif patient_blood == 'IV':
    if donor_blood == 'I' or donor_blood == 'IV': print('blood matches')
    else: print('blood mismatch')