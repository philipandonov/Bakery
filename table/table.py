from abc import ABC, abstractmethod

from bakery.baked_food.baked_food import BakedFood
from bakery.validator.validator import Validator
from bakery.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.value_validation(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def min_value(self):
        pass

    @property
    @abstractmethod
    def max_value(self):
        pass

    @property
    @abstractmethod
    def massage(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.validate_table_number(value, self.min_value, self.max_value, self.massage)
        self.__table_number = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" + \
                   f"Type: {self.__class__.__name__}\n" + \
                   f"Capacity: {self.capacity}"
