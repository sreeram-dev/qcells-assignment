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

    def print_summary_report(self):
        """Print the results from the simulation
        """
        raise NotImplementedError("print the summary report")


