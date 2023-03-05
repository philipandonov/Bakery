from bakery.drink.tea import Tea
from bakery.drink.water import Water


class DrinkFactory:
    def create_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)

