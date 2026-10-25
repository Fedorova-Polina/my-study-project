seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
for name in seq:
    print("Полная последовательность нуклеотидов ДНК: ", name)
    print("Последовательность, разобранная по буквам: ")
    for letter in name:
        print(letter)     
print("Цикл выполнен!")