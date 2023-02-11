# -*- coding:utf-8 -*-
import pytest

from car.factory import PriusFactory, PorscheFactory
from car.models import Car, CarType, CarRoof, ConvertibleCar


class TestCarFactory:

    def test_prius_build(self):
        """
        Should build a non-convertible prius
        :return:
        """
        prius = PriusFactory.build_car()
        assert('Prius' in prius.get_name())
        assert prius.get_car_type() == CarType.NonConvertibleCar
        assert prius.get_hp() == 121
        assert prius.get_mpg() == 53
        assert prius.get_number_of_seats() == 5

    def test_porsche_build(self):
        """
        Should build a porsche boxster with a `CarRoof`
        :return:
        """
        porsche = PorscheFactory.build_car()
        assert('PorscheBoxster' in porsche.get_name())
        assert porsche.get_car_type() == CarType.ConvertibleCar
        assert porsche.get_number_of_seats() == 2
        assert porsche.get_hp() == 265
        assert porsche.get_mpg() == 32

        assert porsche.is_roof_open() is False
        porsche.open_roof()
        assert porsche.is_roof_open() is True
