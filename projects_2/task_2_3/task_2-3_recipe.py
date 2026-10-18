name_culture_medium = input('Введите название питательной среды: ')
agar_concentration = input('Введите концентрацию агара (%): ')
sterilization_temperature = input('Введите температуру стерилизации (°C): ')
with open('C:/Users/Полина/Documents/Fedorova_PA-Practice in vibecoding/projects_2/task_2_3/recipe.txt', 'w', encoding="utf-8") as file:
    file.write(f'{"Название питательной среды:":^40}{name_culture_medium}\n{"Концентрация агара (%):":<35}{agar_concentration}\n{"Температура стерилизации (°C):":<35}{sterilization_temperature}')
print("Файл 'recipe.txt' успешно сформирован!")