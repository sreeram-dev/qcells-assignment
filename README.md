# QCells Interview Assignment

This repository contains the code for the qcells interview assignment.

`todo.md` contains some thoughts on how to make the simulation more realistic.

### Project Layout

* ``car/models.py`` defines the `Porsche` and `PorscheBoxster` classes.
* Additionally, it defines the abstract class, `Car`, and interface, `IConvertibleSpecilization`
* ``car/factory.py`` defines the `PriusFactory` and `PorscheFactory` to build `Prius` and `Porsche` respectively.
* ``parking/parking_lot.py`` defines the interface, `IParkingLotInterface`, and ConcreteClass, `OrderedParkingLot`.

`LRUParkingLot` i.e. `LRU Cache` may be a good addition and meets the assignment specifications, however, may not reflect the real-world scenario.

### Tests

Instructions for the assignment have been implemented as testcases in ``tests/`` folder

* `tests/test_car_factory.py` - Assignment #1 and Assignment #2 - tests the porsche and prius car builds and the `get_description` format string. It also tests the `CarRoof` open and close methods.
* `tests/test_car_race_simulation.py` - Assignment #3 with Porsche car_roof open and acceleration at 20% i.e. 0.2 as value.
* `tests/test_parking_lot.py` - Assignment #4 and Assignment #5 have been defined as two tests to test the OrderedParkingLot. We print the directory at the end of the second test.

## Installation and running tests

### Installation
`pyenv-virtualenv` sets up the sandbox for the assignment.
`.python-version` specifies the python runtime used for the sandbox.

* Run `pip install -r requirements.txt` to install the `pytest` dependency.

### Testing

Run the following commands to execute all tests or individual tests - 

* `pytest tests/ -s` to execute all tests and print the `stdout`.
* `pytest tests/{file} -s` to execute individual test suites. For example, `pytest tests/test_car_factory.py` to execute car builds.
