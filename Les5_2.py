"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

line = 0
try:
    with open("task_2.txt", 'r', encoding='utf-8') as file:
        for str in file:
            if not str:
                break
            line += 1
            words = len((str.split()))
            print(f"{str}слов: {words}")

        print(f"___________________\nколичество строк - {line}")
except IOError:
    print("Произошла ошибка ввода-вывода!")


"""
f = open('text.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()
"""


