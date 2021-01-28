def fact_gen(k):
    fact = 1
    if k == 0:
        yield f'{k}! = 1'
    for i in range(1, k + 1):
        fact *= i
        yield f'{i}! = {fact}'


for el in fact_gen(int(input('Введите номер факториала: '))):
    print(el)