from ProbabilityTools.probabilityCommon import factorial, displayStats
from math import pow, e, sqrt


def showHelp():
    print("A Poisson distribution with mean u, x successes, and a probability of success p\n")
    print("Required arguments:")
    print("---x: the number of successes in a time interval")
    print("---u: the expected number of successes in a time interval")
    print()
    print("Try running:\n\tpython probability.py -pois -x 3 -u 3\n")


def validArgs(argMap: dict) -> bool:
    valid = True
    for arg in ["x", "u"]:
        if argMap.get(arg) is None:
            valid = False
            print(f"\tMissing -{arg} argument")
    return valid


def poisson(x: int, u: float):
    """
    Compute and display a Poisson distribution with x successes and mean u
    :param x: The number of successes
    :param u: The expected number of successes(mean)
    :return:
    """
    if x < 0.0:
        raise ValueError(f"Cannot have less than 0 occurrences in a time interval")
    if u < 0.0:
        raise ValueError(f"Cannot expect less than 0 occurrences in a time interval")

    pmf = (pow(u, x) / factorial(x)) * pow(e, -u)
    cdf = pmf
    for i in range(0, int(x)):
        cdf += (pow(u, i) / factorial(i)) * pow(e, -u)

    displayStats(x, pmf, cdf)

    print(f"---Mean:\t\t{u}")
    print(f"---Variance:\t\t{u}")
    print(f"---Standard Deviation:\t{sqrt(u)}")

