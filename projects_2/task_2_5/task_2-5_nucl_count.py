print('***Анализ последовательности ДНК***\n')
dna = input('Введите последовательность ДНК: ').upper()
count_A = dna.count('A') 
count_C = dna.count('C')
count_G = dna.count('G')
count_T = dna.count('T')
lentgh = len(dna)
content_A = ( count_A / lentgh ) *100
content_C = ( count_C / lentgh ) *100
content_G = ( count_G / lentgh ) *100
content_T = ( count_T / lentgh ) *100
print(f'Последовательность в верхнем регистре: {dna}')
print(f'A: {count_A}\nC: {count_C}\nG: {count_G}\nT: {count_T}')
print(f"Длина всей последовательности ДНК: {lentgh}")
print(f'Содержание нуклеотида A (%): {content_A:.3f}\nСодержание нуклеотида C (%): {content_C:.3f}\nСодержание нуклеотида G (%): {content_G:.3f}\nСодержание нуклеотида T (%): {content_T:.3f}')
