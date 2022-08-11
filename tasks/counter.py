"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value: int

    def __init__(self, some_value = 0):
        self.value = some_value

    def increase(self, num=1):
        self.value += num

    def decrease(self, num=1):
        self.value -= num

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.value += 1
        return value

class_obj = Counter(111)
class_obj.increase()
print(class_obj.value)
class_obj.increase(120)
print(class_obj.value)
class_obj.decrease()
print(class_obj.value)
class_obj.decrease(120)
print(class_obj.value)
count_iter = iter(Counter(10))
print(next(count_iter))
print(next(count_iter))
print(next(count_iter))