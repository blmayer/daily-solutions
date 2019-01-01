"""
    This problem was asked by Google.

    The area of a circle is defined as πr^2. Estimate π to 3 decimal places
    using a Monte Carlo method.

    Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

import random
import math

print(sum([4 if math.pow(random.random(), 2) + math.pow(random.random(), 2) < 1 else 0 for x in range(11000000)])/11000000)
