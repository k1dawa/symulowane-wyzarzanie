import math
from typing import Tuple

#rozdzial 3
def ex3_domain():
    return (-150.0, 150.0)

def ex3_f(x: float):
    if -105 < x < -95:
        return -2 * abs(x + 100) + 10
    elif 95 < x < 105:
        return -2.2 * abs(x - 100) + 11 
    else:
        return 0.0

#rozdzail 4
def ex4_domain():
    return (-1.0, 2.0)

def ex4_f(x: float):
    return x * math.sin(10 * math.pi * x) + 1
