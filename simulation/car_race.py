# -*- coding:utf-8 -*-

from simulation.simulation import ISimulationInterface
from car.builder import CarBuilder


class CarRaceSimulation(ISimulationInterface):
    """Simulation class for the interface
    """

    def __init__(self):
        self.porsche = None
        self.prius = None
        self.results = []

    def initialise_agents(self):
        """Initialise the cars - porsche boxster and prius
        :return:
        """
        self.prius = CarBuilder.build_prius()
        self.porsche = CarBuilder.build_porsche_boxster()

    def run_simulation(self):
        """Run the simulation as given in the document
        :return:
        """

        # open the roof of the porsche boxster
        self.porsche.open_roof()
        assert(self.porsche.is_roof_open() is True)

        epoch = 0
        while self.porsche.get_current_speed() <= 200 and self.prius.get_current_speed() <= 200:
            self.porsche.accelerate(0.2)
            self.prius.accelerate(0.2)
            epoch += 1
            print("epoch: ", epoch, " Prius speed: ", self.prius.get_current_speed(), " Porsche Boxster Speed: ",
                  self.porsche.get_current_speed())
            self.results.append((epoch, self.prius.get_current_speed(), self.porsche.get_current_speed()))

        if self.porsche.get_current_speed() >= 200 > self.prius.get_current_speed():
            print("Porsche Boxster has attained the speed of 200 mph first")
        elif self.prius.get_current_speed() >= 200 > self.porsche.get_current_speed():
            print("Prius has attained the speed of 200 mph first")

    def print_summary_report(self):
        pass



