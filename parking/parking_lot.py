# -*- coding:utf-8 -*-

from abc import ABC

from car.models import Car
from collections import OrderedDict


class IParkingLotInterface:

    def search(self, car: Car) -> int:
        """
        Checks whether the car is present in parking lot or otherwise
        :param car: car to be searched
        :return: -1 if car is not present, else, return parking slot
        """
        raise NotImplementedError

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

    def print_directory(self):
        """
        Prints the parking lot directory
        :return:
        """
        raise NotImplementedError


class OrderedParkingLot(IParkingLotInterface, ABC):

    def __init__(self, capacity):
        """
        Parking slot is a ordered cache with a defined capacity
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
            removed_car, parked_slot = self.directory.popitem(last=False)
            print(f"{removed_car.get_name()} has been removed from slot: {parked_slot}")
            self.dq[parked_slot] = None

        # insert the car in an empty parking slot
        empty_slot = int(min(list(set(range(self.capacity)) - set(self.directory.values()))))
        assert(self.dq[empty_slot] is None)
        self.dq[empty_slot] = car
        self.directory[car] = empty_slot
        print(f"{car.get_name()} has been parked in slot: {empty_slot}")

        return True

    def remove(self, car: Car) -> bool:
        """
        Removes the car if the car is present in parking lot
        :param car:
        :return:
        """
        if car not in self.directory:
            return False

        parked_slot = self.directory[car]
        self.dq[parked_slot] = None
        return True

    def print_directory(self):
        """
        Print the parking lot directory by slot numbers in ascending order
        :return:
        """
        inv_map = {v: k for k, v in self.directory.items()}
        for index in range(self.capacity):
            if index in inv_map:
                print(f"Parking slot: {index}, Car: {inv_map[index].get_name()}")
            else:
                print(f"Parking slot: {index}, Car: EMPTY")
