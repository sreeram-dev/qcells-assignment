# -*- coding:utf-8 -*-

from car.builder import CarBuilder
from parking.parking_lot import OrderedParkingLot


if __name__ == '__main__':
    parking_lot = OrderedParkingLot(2)
    prius_1 = CarBuilder.build_prius()
    prius_2 = CarBuilder.build_prius()
    porsche_1 = CarBuilder.build_porsche_boxster()

    parking_lot.park(prius_1)
    parking_lot.park(prius_2)

    # should raise an error
    try:
        parking_lot.park(porsche_1)
    except KeyError as e:
        print(e)

    parking_lot.park(porsche_1, replace=True)
    prius_2_slot = parking_lot.search(prius_2)
    assert(parking_lot.search(prius_2) == -1)
    # prius_1 is parked first
    assert(parking_lot.search(prius_1) != -1)
    assert(parking_lot.search(porsche_1) != -1)