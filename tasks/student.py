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

    def __init__(self, some_surname, some_name, some_group, some_average_score):
        self.surname=some_surname
        self.name=some_name
        self.group=some_group
        self.average_score=some_average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __eq__(self, other):
        return self.average_score == other.average_score
sorted_student_list_2 = []
sorted_student_list_1 = []
student_1=Student("surname1", "name1", 5, 7.6)
student_2=Student("surname2", "name2", 3, 9.6)
student_3=Student("surname3", "name3", 1, 4.6)
student_4=Student("surname4", "name4", 2, 7.3)
student_5=Student("surname5", "name5", 3, 7.7)
student_list=[student_1, student_2, student_3, student_4, student_5]
for i in sorted(student_list):
    sorted_student_list_1.append(i.name)
for i in sorted(student_list, reverse=True):
    sorted_student_list_2.append(i.name)
print(sorted_student_list_1)
print(sorted_student_list_2)
for i in student_list:
    if i.average_score>5.0:
        print(i.name)