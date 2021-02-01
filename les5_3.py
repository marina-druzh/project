"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
"""
with open('task_3.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    low_sal = []
    my_list = my_file.read().split('\n')
    print('Меньше 20.000 получают:')
    for i in my_list:
        i = i.split()
        salary.append(i[1])
        if float(i[1]) < 20000:
            low_sal.append(i[0])
            print(i[0])
    print(f'Cредний оклад: {sum(map(int, salary)) / len(salary)}')






