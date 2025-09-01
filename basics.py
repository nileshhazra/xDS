numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

from functools import partial


def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8]
