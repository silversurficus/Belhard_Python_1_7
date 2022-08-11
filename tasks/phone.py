"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, some_brand, some_model, some_issue_year):
        self.brand = some_brand
        self.model = some_model
        self.issue_year = some_issue_year

    def receive_call(self, name):
        print(f"Звонит {name}")

    def get_info(self):
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return "Бренд: {} \nМодель: {} \nГод выпуска: {}".format(self.brand, self.model, self.issue_year)
