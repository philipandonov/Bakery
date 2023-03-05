from bakery.validator.drink_factory import DrinkFactory
from bakery.validator.food_factory import FoodFactory
from bakery.validator.table_factory import TableFactory
from bakery.validator.validator import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drink_menu = []
        self.table_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.name_validate_for_empty_and_white_spaces(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any(d.name == name for d in self.drink_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.drink_factory.create_drink(drink_type, name, portion, brand)
        self.drink_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any(t.table_number == table_number for t in self.table_repository):
            raise Exception("Table {table_number} is already in the bakery!")
        table = self.table_factory.create_table(table_type, table_number, capacity)
        self.table_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.table_repository:
            if table.is_reserved:
                continue
            if number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: []):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        ordered_foods = f"Table {table_number} ordered:\n"
        skipped_ordered_foods = f'{self.name} does not have in the menu:\n'
        for food_name in food_names:
            food = self.find_food(food_name)
            if food is None:
                skipped_ordered_foods += food_name + '\n'
            else:
                ordered_foods += str(food) + '\n'
                table.order_food(food)
        return ordered_foods + skipped_ordered_foods.strip()

    def find_table_by_number(self, table_number):
        for table_num in self.table_repository:
            if table_num.table_number == table_number:
                return table_num
        return None

    def find_food(self, food_name):
        for food in self.food_menu:
            if food_name == food.name:
                return food
        return None

    def find_drink(self, drink_name):
        for drink in self.drink_menu:
            if drink_name == drink.name:
                return drink
        return None

    def order_drink(self, table_number: int, *drinks_name: []):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        ordered_drinks = f"Table {table_number} ordered:\n"
        skipped_ordered_drinks = f'{self.name} does not have in the menu:\n'
        for drink_name in drinks_name:
            drink = self.find_drink(drink_name)
            if drink is None:
                skipped_ordered_drinks += drink_name + '\n'
            else:
                ordered_drinks += str(drink) + '\n'
                table.order_drink(drink)
        return ordered_drinks + skipped_ordered_drinks.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" + f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.table_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
