# -*- coding:utf-8 -*-
import pytest

from car.factory import PriusFactory, PorscheFactory
from parking.parking_lot import OrderedParkingLot


class TestParkingLot:
    def test_with_2_slots_and_3_cars_raises_exception(self):
        """
        Assignment #4
        :return:
        """
        parking_lot = OrderedParkingLot(2)
        prius_1 = PriusFactory.build_car()
        prius_2 = PriusFactory.build_car()
        porsche_1 = PorscheFactory.build_car()

        parking_lot.park(prius_1)
        parking_lot.park(prius_2)

        with pytest.raises(KeyError) as e_info:
            parking_lot.park(porsche_1)
            assert e_info == "The parking lot is at full capacity"

    def test_with_3_slots_and_2_cars_with_replace(self):
        """
        Assignment #5
        :return:
        """
        # test setup
        parking_lot = OrderedParkingLot(3)
        prius_1 = PriusFactory.build_car()
        prius_2 = PriusFactory.build_car()
        parking_lot.park(prius_1)
        parking_lot.park(prius_2)

        porsche_1 = PorscheFactory.build_car()
        parking_lot.park(porsche_1)
        assert parking_lot.search(porsche_1) != -1

        prius_3 = PriusFactory.build_car()
        parking_lot.park(prius_3, replace=True)
        # prius_3 has been parked in the place of prius_1
        assert parking_lot.search(prius_1) == -1
        assert parking_lot.search(prius_3) != -1

        porsche_2 = PorscheFactory.build_car()
        parking_lot.park(porsche_2, replace=True)
        # porsche_2 has been parked in place of prius_2
        assert parking_lot.search(prius_2) == -1
        assert parking_lot.search(porsche_2) != -1

        # finally print the directory
        print("### PRINTING THE DIRECTORY ###")
        parking_lot.print_directory()
