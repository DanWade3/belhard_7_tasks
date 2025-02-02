"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname: str, name: str, group: int, average_score: float):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __repr__(self):
        return f"<Student surname={self.surname}, score={self.average_score}>"


students_list = [
    Student('a', 'a', 123, 5.6),
    Student('b', 'b', 123, 7.7),
    Student('c', 'c', 123, 5.6),
    Student('d', 'd', 123, 9.2),
    Student('e', 'e', 123, 8)
]

print(sorted(students_list))
print(sorted(students_list, reverse=True))
