from typing import List


class BaseField:
    my_type = str

    def __init__(self, name, value, weight=1):
        self.check_name(name)
        self.check_value(value)
        self.check_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

    @staticmethod
    def check_name(name):
        if isinstance(name, str):
            return name
        raise TypeError('Ошибка - введите, пожалуйста, в буквенном значении')

    @staticmethod
    def check_weight(weight):
        if isinstance(weight, int):
            return weight
        raise TypeError('Ошибка')

    def check_value(self, value):
        if isinstance(value, self.my_type):
            return value
        raise TypeError('Ошибка')


class StringField(BaseField):
    my_type = str


class SearchParams:
    def __init__(self, fields: List[BaseField]) -> None:
        self.registry = dict()
        for field in fields:
            self.registry[field.name] = field
