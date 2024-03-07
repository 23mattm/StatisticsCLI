import math
from math import pow

from ProbabilityTools.probabilityCommon import choose, displayStats


def validArgs(argMap: dict) -> bool:
    valid = True
    for arg in ["n", "x", "p"]:
        if argMap.get(arg) is None:
            valid = False
            print(f"\tMissing -{arg} argument")
    return valid


def showHelp():
    print("A negative binomial distribution with the xth success being the nth trial with a probability of success p\n")
    print("Required arguments:")
    print("---x: the number of successes")
    print("---n: the number of total trials")
    print("---p: the probability of a success, [0.0, 1.0]")
    print()
    print("Try running:\n\tpython probability.py -nbin -x 5 -n 10 -p 0.5\n")


def nbinDist(x: int, n: int, p: float):
    """
    Compute and display probabilities using a negative binomial distribution
    :param x: The number of successes
    :param n: The total number of trials
    :param p: The probability of a success
    :return:
    """
    if x > n:
        raise ValueError(f"Number of successes, X = {x}, cannot exceed the number of trials, n = {n}")
    if p < 0.0 or p > 1.0:
        raise ValueError(f"Probability({p}) must be [0,1]")

    print(f"Negative binomial distribution with {x}th success on the {n}th trial and a p(x) = {p}:\n")

    q = 1.0 - p

    pmf = choose(n-1, x-1) * pow(p, x) * pow(q, n-x)
    cdf = pmf
    for i in range(1, int (x)):
        cdf += choose(n-1, i-1) * pow(p, i) * pow(q, n-i)

    displayStats(x, pmf, cdf)

    variance = x * q / pow(p, 2)

    print(f"---Mean:\t\t{x/p}")
    print(f"---Variance:\t\t{variance}")
    print(f"---Standard Deviation:\t{math.sqrt(variance)}")

