# -*- coding:utf-8 -*-

from simulation.simulation import ISimulationInterface
from car.factory import PriusFactory, PorscheFactory


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
        self.prius = PriusFactory.build_car()
        self.porsche = PorscheFactory.build_car()

    def run_simulation(self):
        """Run the simulation as given in the document
        :return:
        """

        # open the roof of the porsche boxster
        self.porsche.open_roof()
        assert self.porsche.is_roof_open() is True

        epoch = 0
        while self.porsche.get_current_speed() <= 200 and self.prius.get_current_speed() <= 200:
            self.porsche.accelerate(0.2)
            self.prius.accelerate(0.2)
            epoch += 1
            self.print_epoch_result(epoch)
            self.results.append((epoch, self.prius.get_current_speed(), self.porsche.get_current_speed()))

        if self.porsche.get_current_speed() >= 200 > self.prius.get_current_speed():
            print(f"{self.porsche.get_name()} has attained the speed of 200 mph first")
        elif self.prius.get_current_speed() >= 200 > self.porsche.get_current_speed():
            print(f"{self.prius.get_name()} has attained the speed of 200 mph first")
        else:
            print(f"Both {self.porsche.get_name()} and {self.prius.get_name()} have attained the speed of 200 mph")

    def print_epoch_result(self, epoch: int):
        print(f"Epoch: {epoch}, {self.porsche.get_name()} Speed: {self.porsche.get_current_speed()},\
                {self.prius.get_name()} Speed: ", self.prius.get_current_speed())



