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
    sequence: list
    n: int

    def __init__(self, n: int, sequence: list):
        self.n = n
        self.sequence = sequence

    def generate(self):
        for _ in range(self.n):
            self.sequence.append(random.randint(-10, 10))
            return self.sequence

    def print_seq(self):
        print(self.sequence)


print(random.uniform(-10, 5))
