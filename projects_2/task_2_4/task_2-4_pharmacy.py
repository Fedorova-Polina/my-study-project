number_capsules = int(input('Введите общее количество произведенных капсул: ') )
capacity = int(input('Введите количество капсул в одной упаковке: ') )
number_packages = number_capsules // capacity 
remainder = number_capsules % capacity
print('--- Отчет фасовочного цеха ---') 
print(f'Полных упаковок: {number_packages}\nОстаток капсул: {remainder}')