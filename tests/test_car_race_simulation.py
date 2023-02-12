# -*- coding:utf-8 -*-

from simulation.car_race import CarRaceSimulation
from car.models import Car, CarType


class TestCarSimulation:

    def test_car_race_porsche_wins(self):
        print("\n ### CAR RACE SIMULATION ###")
        simulation = CarRaceSimulation()
        simulation.initialise_agents()
        winner: Car = simulation.run_simulation()
        # assert winner is porsche
        assert "PorscheBoxster" in winner.get_name()
        assert winner.get_car_type() == CarType.ConvertibleCar
