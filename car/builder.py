# -*- coding:utf-8 -*-

from car.models import Car, ConvertibleCar, CarEngine


class CarBuilder:
    @staticmethod
    def build_prius() -> Car:
        engine = CarEngine(121, 53)

        car = Car()
        car.set_name("Prius")
        car.set_number_of_seats(5)
        car.set_current_speed(0)
        car.set_production_number("a#789")
        car.set_engine(engine)

        return car

    @staticmethod
    def build_porsche_boxster() -> ConvertibleCar:
        engine = CarEngine(265, 32)

        car = ConvertibleCar()
        car.set_name("PorscheBoxster")
        car.set_number_of_seats(2)
        car.set_current_speed(0)
        car.set_production_number("b#678")
        car.set_engine(engine)

        return car
