from sys import argv

try:
    id, rate, time, bonus = map(float, argv[1:])
    print("Табельный №:         Запрплата:\n", int(id), ' ' * 15, rate * time + bonus)
except ValueError:
    print("Все 4 аргумента должны быть числами")
