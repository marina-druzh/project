'''
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

str = (input('Введите несколько элементов списка '))
my_list = str.split()
i = 0
while i <= len(my_list)-1:
    el = my_list.pop(i)
    my_list.insert(i + 1, el)
    i = i + 2
print(my_list)


'''
spisok = ['gh', 'tyt', 677, 55, 'tt']
for index in range(len(spisok)//2):
    spisok[index], spisok[-(index+1)] = spisok[-(index+1)], spisok[index]
print(spisok)
'''
