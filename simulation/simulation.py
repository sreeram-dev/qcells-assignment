# -*- coding:utf-8 -*-


class ISimulationInterface:

    def initialise_agents(self):
        """Initialise the agents used in the system
        """
        raise NotImplementedError("agents have not been initialised")

    def run_simulation(self):
        """Initialise the simulation
        """
        raise NotImplementedError("define the simulation")

    def print_epoch_result(self, epoch: int):
        """Print the results from the simulation
        """
        raise NotImplementedError("print the epoch result")


