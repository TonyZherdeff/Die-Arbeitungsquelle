print("Задание 1")
with open("Text1.txt") as file1:
    f = list(file1.readlines())
with open("Text2.txt") as file2:
    f_new = list(file2.readlines())
i = 0
while i < len(f):
    if f[i] != f_new[i]:
        print(f'Содержимое строки {i+1} в файле 1 {f[i]}')
        print(f'Содержимое строки {i+1} в файле 2 {f_new[i]}')
    i += 1
file1.close()
file2.close()

print("Задание 2")
with open("Text1_1.txt") as file1:
    list_f = list(file1.readlines())
    string_f = ""
    v_letters = "уеыаоэёяию"
    c_letters = "йцкнгшщзхъфвпрлджчсмтьб"
    nums = "0123456789"
    v_let_count = 0
    c_let_count = 0
    num_count = 0
    for i in list_f:
        string_f = string_f + i.lower()
    for i in string_f:
        if i in v_letters:
            v_let_count += 1
        elif i in c_letters:
            c_let_count += 1
        elif i in nums:
            num_count += 1
    log_file = open("Text1_2.txt", 'w+')
    log_file.write(f'Количество символов в файле равно {len(string_f)}\n')
    log_file.write(f'Количество строк в файле равно {len(list_f)}\n')
    log_file.write(f'Количество гласных букв в файле равно {v_let_count}\n')
    log_file.write(f'Количество согласных букв в файле равно {c_let_count}\n')
    log_file.write(f'Количество цифр в файле равно {num_count}\n')
    log_file.close()
log_file = open("Text1_2.txt", 'r')
print(log_file.read())
log_file.close()
file1.close()

print("Задание 3")
with open("Text2_1.txt", "r") as file:
    list_l = list(file.readlines())
    print(list_l)
file.close()
with open("Text2_1.txt", "w") as file1:
    i = 0
    while i < len(list_l) - 1:
        file1.write(list_l[i])
        i += 1
fil = open("Text2_2.text", 'w+')
fil.write(f'{list_l[i]}\n')
fil.close()
fil1 = open("Text2_2.text", 'r')
print("Удлена строка", fil1.read())
fil1.close()
file1.close()
with open("Text2_1.txt", "r") as file2:
    list_l = list(file2.readlines())
    print(list_l)
file2.close()

print("Задание 4")
with open("Text1_1.txt", "r") as file:
    list_l = list(file.readlines())
    i = 0
    s = ""
    while i < len(list_l):
        if len(list_l[i]) > len(s):
            s = list_l[i]
        i += 1
    print(f'Длина самой длинной строки равна {len(s)}')
file.close()

import re


print("Задание 5")
with open("Text1_1.txt", "r") as file:
    list_l = list(file.readlines())
    word = str(input("Введите слово для посика\n").lower())
    count = 0
    for i in list_l:
        x = re.split(" ", i.lower())
        if word in x:
            count += 1
    print(f'Слово {word} встречается в тексте {count} раз(а)')
file.close()

print("Задание 6")
with open("Text1_1.txt", "r") as file1:
    list_l = list(file1.readlines())
    list_l_1 = []
    word = str(input("Введите слово для посика\n"))
    word1 = str(input("Введите слово для замены\n"))
    for i in list_l:
        x = re.split(" ", i)
        j = 0
        while j < len(x):
            if x[j] == word:
                x[j] = word1
            j += 1
        list_l_1.append(" ".join(x))
file1.close()
with open("Text3.txt", "w") as file2:
    for i in list_l_1:
        file2.write(i)
file2.close()
file3 = open("Text3.txt", "r")
print(file3.read())
file3.close()