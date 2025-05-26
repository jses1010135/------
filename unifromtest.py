import random as r
def uniform_test():
    value = int(r.uniform(1, 100))
    value2= round(r.gauss(50, 15))  # Normal distribution with mean=50, stddev=15
    value2=max(0, min(100, value2))  # Ensure value2 is at least 1 and at most 100
    if value < 1 or value > 100:
        raise ValueError("Value is out of range: {}".format(value))
    