volume_solution = float(input('Введите нужный объем раствора (мл): '))
salt_mass = volume_solution * 0.009
with open('C:/Users/Полина/Documents/Fedorova_PA-Practice in vibecoding/projects_2/task_2_4/recipe.txt', 'w', encoding='utf-8') as file:
          file.write('ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ: \n')
          file.write('=' * 30 + '\n')
          file.write(f'{"Общий объем раствора: ":<27}{volume_solution} мл\n{"Масса соли: ":<27}{salt_mass:.3f} г\n{"Объем воды: ":<27}{volume_solution} мл')