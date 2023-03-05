from bakery.baked_food.bread import Bread
from bakery.baked_food.cake import Cake


class FoodFactory:
    def create_food(self, food_type: str, name: str, price: float):
        if food_type == 'Cake':
            return Cake(name, price)
        elif food_type == "Bread":
            return Bread(name, price)
