class MovingTotal:

    numbers = []
    totals = set()

    def append(self, new_numbers):
        """
        :param new_numbers: (list) The list of numbers.
        """
        for new_number in new_numbers:
            self.numbers.append(new_number)
            if len(self.numbers) >= 3:
                self.totals.add(self.numbers[-3] + self.numbers[-2] + self.numbers[-1])

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.totals


movingtotal = MovingTotal()
movingtotal.append([5, 5, 5])
print(movingtotal.contains(15))
print(movingtotal.contains(9))
movingtotal.append([1])
print(movingtotal.contains(11))
movingtotal.append([1, 2, 3])
