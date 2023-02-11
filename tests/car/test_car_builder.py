# -*- coding:utf-8 -*-
import pytest

from car.factory import CarBuilder
from car.models import Car


class TestCarBuilder:

    def test_prius_build(self):
        """
        Should build a non-convertible prius
        :return:
        """

        CarBuilder
