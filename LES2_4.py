'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово
длинное, выводить только первые 10 букв в слове.
'''
str = (input('Введите строку, состоящую из нескольких слов ').split())
for i in str:
    el = i
    if len(el) > 10:
       el = el[:10]
    print(str.index(i), el)

