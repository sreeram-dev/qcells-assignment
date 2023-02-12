# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from car.models import CarEngine, Prius, PorscheBoxster
from car.utils import generate_random_string


class CarFactory(ABC):

    @abstractmethod
    def build_default_model(self):
        pass


class PriusFactory(CarFactory):

    @staticmethod
    def build_default_model() -> Prius:
        engine = CarEngine(121, 53)

        car = Prius()
        car.set_name(f"Prius#{generate_random_string(4)}")
        car.set_number_of_seats(5)
        car.set_current_speed(0)
        car.set_production_number(generate_random_string())
        car.set_engine(engine)

        return car


class PorscheFactory(CarFactory):

    @staticmethod
    def build_default_model() -> PorscheBoxster:
        engine = CarEngine(265, 32)

        car = PorscheBoxster()
        car.set_name(f"PorscheBoxster#{generate_random_string(4)}")
        car.set_number_of_seats(2)
        car.set_current_speed(0)
        car.set_production_number(generate_random_string())
        car.set_engine(engine)

        return car
