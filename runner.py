# -*- coding:utf-8 -*-

from simulation.car_race import CarRaceSimulation

if __name__ == '__main__':
    simulation = CarRaceSimulation()
    simulation.initialise_agents()
    simulation.run_simulation()


