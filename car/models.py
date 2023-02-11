# -*- coding:utf-8 -*-

from enum import Enum


class CarRoof(Enum):
    CLOSED = 1
    OPEN = 2


class CarType(Enum):
    """
    Convertible Cars have a `CarRoof`
    """
    ConvertibleCar = 1
    NonConvertibleCar = 2


class CarEngine:
    def __init__(self, hp: float, mpg: float):
        """
        Car engine has two parameters - horsepower and miles per gallon
        """
        self._hp = hp
        self._mpg = mpg

    def get_hp(self) -> float:
        return self._hp

    def get_mpg(self) -> float:
        return self._mpg


class IConvertibleSpecialization:

    def open_roof(self):
        """
        Open the roof of the car
        """
        raise NotImplementedError("open roof method is not defined")

    def close_roof(self):
        """
        Close the roof of the car
        """
        raise NotImplementedError("close roof method is not defined")

    def is_roof_open(self) -> bool:
        raise NotImplementedError


class Car:

    def __init__(self):
        self._engine = None
        self._production_number = None
        self._current_speed = None
        self._no_of_seats = None
        self._name = None
        self._car_type = CarType.NonConvertibleCar

    def set_name(self, name: str):
        self._name = name

    def set_number_of_seats(self, no_of_seats: int):
        self._no_of_seats = no_of_seats

    def set_current_speed(self, current_speed: float = 0.0):
        self._current_speed = current_speed

    def get_current_speed(self) -> float:
        return self._current_speed

    def set_production_number(self, production_number: str):
        self._production_number = production_number

    def set_engine(self, engine: CarEngine):
        self._engine = engine

    def get_name(self) -> str:
        return self._name

    def get_number_of_seats(self) -> int:
        return self._no_of_seats

    def get_hp(self) -> float:
        return self._engine.get_hp()

    def get_mpg(self) -> float:
        return self._engine.get_mpg()

    def get_production_number(self) -> str:
        return self._production_number

    def get_car_type(self) -> CarType:
        return self._car_type

    def get_description(self) -> str:
        return f" Name: {self.get_name()} \n" \
               f" Car Type: {self.get_car_type()} \n" \
               f" Production Number: {self.get_production_number()} \n" \
               f" Horse Power: {self.get_hp()}hp"

    def accelerate(self, accelerate: float):
        """
        Accelerates / Decelerates the car

        :param accelerate:
        :return:
        """
        assert (1.0 >= accelerate >= -1.0)
        hp = self.get_hp()
        velocity_over_epoch = hp * accelerate
        self.set_current_speed(self.get_current_speed() + velocity_over_epoch)


class ConvertibleCar(Car, IConvertibleSpecialization):

    def __init__(self):
        super().__init__()
        self._roof = CarRoof.CLOSED
        self._car_type = CarType.ConvertibleCar

    def open_roof(self):
        if self._roof == CarRoof.OPEN:
            print("The car roof is currently open")
        else:
            print("Opening the roof of the ", self.get_name())
            self._roof = CarRoof.OPEN

    def close_roof(self):
        if self._roof == CarRoof.CLOSED:
            print("The car roof is currently closed")
        else:
            print("Closing the roof of the ", self.get_name())
            self._roof = CarRoof.CLOSED

    def is_roof_open(self) -> bool:
        return self._roof == CarRoof.OPEN
