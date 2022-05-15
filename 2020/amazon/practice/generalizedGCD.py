def generalizedGCD(length_of_numbers, numbers):
    numbers = sorted(numbers)
    potential_greatest_common_divisor = numbers[-1]
    while potential_greatest_common_divisor > 0:
        if all([number % potential_greatest_common_divisor == 0 for number in numbers]):
            return potential_greatest_common_divisor
        else:
            potential_greatest_common_divisor -= 1


if __name__ == '__main__':
    print(generalizedGCD(5, [2, 3, 4, 5, 6]))
    assert(generalizedGCD(5, [2, 3, 4, 5, 6]) == 1)

    print(generalizedGCD(5, [2, 4, 6, 8, 10]))
    assert(generalizedGCD(5, [2, 4, 6, 8, 10]) == 2)
