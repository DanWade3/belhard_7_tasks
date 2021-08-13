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
    current: int

    def __init__(self, start: int = 0):
        self.current = start

    def increase(self):
        add_number = self.current
        self.current += 1
        return add_number

    def decrease(self):
        dec_number = self.current
        self.current -= 1
        return dec_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 10:
            raise StopIteration
        current = self.current
        self.increase()
        return current


current = Counter()

for item in current:
    print(item)
