'''
    3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
    и возвращает сумму наибольших двух аргументов.
'''
def my_f(var_1, var_2, var_3):
    try:
        list = [var_1, var_2, var_3]
        list.sort()           #Сортировка списка по возрастанию
        sum = list[1]+list[2]
        return f"Сумма 2-х наиольших чисел: {sum}"
    except TypeError:
        return "Enter only a numbers!"


print(my_f(-4, 6, -50))