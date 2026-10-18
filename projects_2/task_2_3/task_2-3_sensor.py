operator_name = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па): ')
with open('C:/Users/Полина/Documents/Fedorova_PA-Practice in vibecoding/projects_2/task_2_3/sensor_log.txt', 'w', encoding='utf-8') as file:
    file.write(f'{operator_name}\t{pressure}')
print('Данные успешно сохранены в sensor_log.txt')