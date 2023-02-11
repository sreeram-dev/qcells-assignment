# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from car.models import Car, ConvertibleCar, CarEngine
from car.utils import generate_random_string


class CarFactory(ABC):

    @abstractmethod
    def build_car(self):
        pass


class PriusFactory(CarFactory):

    @staticmethod
    def build_car() -> Car:
        engine = CarEngine(121, 53)

        car = Car()
        car.set_name(f"Prius#{generate_random_string(4)}")
        car.set_number_of_seats(5)
        car.set_current_speed(0)
        car.set_production_number(generate_random_string())
        car.set_engine(engine)

        return car


class PorscheFactory(CarFactory):

    @staticmethod
    def build_car() -> ConvertibleCar:
        engine = CarEngine(265, 32)

        car = ConvertibleCar()
        car.set_name(f"PorscheBoxster#{generate_random_string(4)}")
        car.set_number_of_seats(2)
        car.set_current_speed(0)
        car.set_production_number(generate_random_string())
        car.set_engine(engine)

        return car
