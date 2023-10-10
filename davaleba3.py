class Car:
    def __init__(self, brand: str, model: str, production_year: int, color: str, horse_power: int, is_sport_car: bool = False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    def get_brand(self) -> str:
        return self.__brand

    def get_model(self) -> str:
        return self.__model

    def get_production_year(self) -> int:
        return self.__production_year

    def get_color(self) -> str:
        return self.__color

    def get_horse_power(self) -> int:
        return self.__horse_power

    def is_sport_car(self) -> bool:
        return self.__is_sport_car

    def change_color(self, new_color: str) -> bool:
        if new_color != self.get_color():
            self.__color = new_color
            return True
        else:
            return False

    def increase_horse_power(self, hp: int) -> bool:
        if hp > 0:
            self.__horse_power += hp
            return True
        else:
            return False
    def increase_horse_power(self, hp: int) -> bool:
        if hp <= 0:  
            return False
        else:
            self.__horse_power += hp
            return True

    def __str__(self):
        return f"Brand: {self.get_brand()} Model: {self.get_model()} Production Year: {self.get_production_year()} Color: {self.get_color()} Horse Power: {self.get_horse_power()} Is Sport Car: {self.is_sport_car()}"