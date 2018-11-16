class CargoShip:

    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity

    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        cargo_to_be_unloaded = []

        cargo_index = 0
        while cargo_index < len(self.cargo):
            if self.cargo[cargo_index][0] == port:
                cargo_to_be_unloaded.append(self.cargo.pop(cargo_index))
            else:
                cargo_index += 1  # We only want to increment if we're *not* popping out a cargo item.
        return cargo_to_be_unloaded

    def can_depart(self):
        """
        :returns: (Bool)
        """
        return sum([cargo_item[1] for cargo_item in self.cargo]) <= self.capacity

    def load(self, new_cargo):
        """
        :param new_cargo: [(String, Int)]
        """
        self.cargo += new_cargo


ship = CargoShip(10)
ship.load([("New York", 1), ("London", 20)])
print(ship.unload("New York"))  # should print [("New York", 1)]
print(ship.cargo)  # should print [("London", 20)]
print(ship.can_depart())  # should print False