# -*- coding:utf-8 -*-

import random

from abc import ABC

from car.models import Car
from collections import OrderedDict


class IParkingLotInterface:

    def park(self, car: Car) -> bool:
        """
        Park the car in the parking lot
        :param car:
        :return: if the parking of the car was successful
        """
        raise NotImplementedError

    def remove(self, car: Car) -> bool:
        """
        Remove the car from the parking lot
        :param car: the car to be removed from parking lot
        :return: if the removal of the car was successful
        """
        raise NotImplementedError


class ParkingSlot:

    def __init__(self, slot: int):
        self.slot = slot
        self.car = None

    def is_empty(self) -> bool:
        return self.car is None

    def park(self, car: Car):
        """
        Park i.e. store a car in the parking slot
        :param car:
        :return:
        """
        self.car = car

    def remove(self):
        """
        Remove the car if parked, from the parking slot
        :return:
        """
        self.car = None


class OrderedParkingLot(IParkingLotInterface, ABC):

    def __init__(self, capacity):
        """
        Parking slot is a lru cache with a defined capacity
        :param capacity:
        """
        self.capacity = capacity
        self.directory = OrderedDict()
        self.dq = [None for _ in range(self.capacity)]

    def search(self, car: Car) -> int:
        """
        Find the parking slot for the car
        :param car:
        :return: parking slot if the car is parked in the parking lot
        """
        if car in self.directory:
            return self.directory[car]

        return -1

    def park(self, car: Car, replace=False) -> bool:
        """
        Park a car in the parking lot
        :param car: car to be parked
        :param replace: if the parking lot is full, remove a car and park the incoming car
        :return: True if the parking is successful
        """

        if len(self.directory.keys()) == self.capacity:
            # do not remove the least recently used parking slot
            if not replace:
                raise KeyError("The parking lot is at full capacity")
            # remove the oldest car parked in the parking lot
            removed_car, parked_slot = self.directory.popitem()
            print(f"Removed car: {removed_car.get_name()} parked_slot: {parked_slot}")
            self.dq[parked_slot] = None

        # insert the car in an empty parking slot
        empty_slot = min(list(set(range(self.capacity)) - set(self.directory.values())))
        assert(self.dq[empty_slot] is None)
        self.dq[empty_slot] = car
        self.directory[car] = empty_slot

        return True

    def remove(self, car: Car) -> bool:
        """
        Removes the car if the
        :param car:
        :return:
        """
        if car not in self.directory:
            return False

        parked_slot = self.directory[car]
        self.dq[parked_slot] = None
        return True



