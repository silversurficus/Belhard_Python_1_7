"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random

class RandSequence:
    n: int
    sequence: list

    def __init__(self, some_n):
        self.sequence = random.sample(range(-some_n, some_n), some_n)

    def generate(self, some_n):
        self.sequence = []
        for i in range(some_n):
            k = random.randint(-some_n, some_n)
            self.sequence.append(k)

    def print_seq(self):
        print(f"{self.sequence}")

