"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title="ordinary"):
        self.title = title

    def draw(self):
        print(f"Let's take one {self.title} quill and start drawing! ))")


class Pen(Stationery):

    def draw(self, color=''):
        print(f"Take one {color} {self.title} pen and start drawing!")


class Pencil(Stationery):

     def draw(self, color="blue"):
         print(f"Take one {color} {self.title} pencil and start drawing!")


class Marker(Stationery):

    def draw(self, color="yellow"):
        print(f"Take one {color} {self.title} marker and start drawing!")


take = Stationery()
take.draw()
pen = Pen()
pen.draw()
pen = Pen("Parker")
pen.draw("red")
pencil = Pencil('watercolor')
pencil.draw()
marker = Marker()
marker.draw('purple')
