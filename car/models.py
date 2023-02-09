# -*- coding:utf-8 -*-

from enum import Enum


class CarEngine:
    def __init__(self, hp: float, mpg: float):
        """Car engine has two parameters - horse power and miles per gallon
        """
        self.hp = hp
        self.mpg = mpg

    def get_hp(self):
        return self.hp

    def get_mpg(self):
        return self.mpg


class IConvertibleSpecialization:

    def open_roof(self):
        """Open the roof of the car
        """
        raise NotImplementedError("open roof method is not defined")

    def close_roof(self):
        """Close the roof of the car
        """
        raise NotImplementedError("close roof method is not defined")

    def is_roof_open(self) -> bool:
        raise NotImplementedError

    def is_roof_closed(self) -> bool:
        raise NotImplementedError


class CarRoof(Enum):
    CLOSED = 1
    OPEN = 2


class Car:

    def __init__(self):
        self.engine = None
        self.production_number = None
        self.current_speed = None
        self.no_of_seats = None
        self.name = None

    def set_name(self, name: str):
        self.name = name

    def set_number_of_seats(self, no_of_seats: int):
        self.no_of_seats = no_of_seats

    def set_current_speed(self, current_speed: float = 0.0):
        self.current_speed = current_speed

    def get_current_speed(self) -> float:
        return self.current_speed

    def set_production_number(self, production_number: str):
        self.production_number = production_number

    def set_engine(self, engine: CarEngine):
        self.engine = engine

    def accelerate(self, accelerate: float):
        """Accelerates / Decelerates the car

        :param accelerate:
        :return:
        """
        assert(1.0 >= accelerate >= -1.0)
        hp = self.engine.get_hp()
        velocity_over_epoch = hp*accelerate
        self.current_speed = self.current_speed + velocity_over_epoch


class ConvertibleCar(Car, IConvertibleSpecialization):

    def __init__(self):
        super().__init__()
        self.roof = CarRoof.CLOSED

    def open_roof(self):
        if self.roof == CarRoof.OPEN:
            print("The car roof is currently open")
        else:
            print("Opening the roof of the ", self.name)
            self.roof = CarRoof.OPEN

    def close_roof(self):
        if self.roof == CarRoof.CLOSED:
            print("The car roof is currently closed")
        else:
            print("Closing the roof of the ", self.name)
            self.roof = CarRoof.CLOSED

    def is_roof_open(self) -> bool:
        return self.roof == CarRoof.OPEN

    def is_roof_closed(self) -> bool:
        return self.roof == CarRoof.CLOSED
