name_researcher = input('Введите имя исследователя: ')
date = input('Введите дату проведения эксперимента: ')
name_experiment = input('Введите название эксперимента: ')
conclusion = input('Ключевой вывод: ')
with open('C:/Users/Полина/Documents/Fedorova_PA-Practice in vibecoding/projects_2/task_2_3/journal.txt', 'w', encoding='utf-8') as file:
    file.write('#' + '*' * 75 + '#\n')
    file.write(f"|{'Электронный лабораторный журнал':^75}|\n")
    file.write('#' + '*' * 75 + '#\n')
    file.write(f"|{'ФИО исследователя:':<20}{name_researcher:<55}|\n")
    file.write(f"|{'Дата:':<20}{date:<55}|\n")
    file.write(f"|{'Эксперимент:':<20}{name_experiment:<55}|\n")
    file.write('#' + '*' * 75 + '#\n')
    file.write(f"|{'Вывод:':<75}|\n")
    import textwrap
    wrapped_lines = textwrap.wrap(conclusion, width=73)
    for line in wrapped_lines:
            file.write(f"| {line:<73} |\n")
    file.write('#' + '*' * 75 + '#\n') 