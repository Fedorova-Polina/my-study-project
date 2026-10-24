donor_blood = input('Введите группу крови ((I, II, III, IV): ').strip().upper()
patient_blood = input('Введите группу крови ((I, II, III, IV): ').strip().upper()
if donor_blood == patient_blood or donor_blood == 'I':
    print("Возможно переливание донорской крови")
else:
    print('Переливание крови донора пациенту абсолютно невозможно')