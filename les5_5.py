"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def task_5():
    from random import randint
    with open('task_5.txt', 'w+', encoding='utf-8') as f_obj:
        my_list = [randint(1, 1000) for _ in range(50)]
        f_obj.write(" ".join(map(str, my_list)))
        f_obj.seek(0)
        return sum(map(int, f_obj.read().split()))


print('Сумма чисел в файле:', task_5())
