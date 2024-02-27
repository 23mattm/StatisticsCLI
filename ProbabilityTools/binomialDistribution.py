from math import pow

from ProbabilityTools import probabilityCommon


def validArgs(argMap: dict) -> bool:
    valid = True
    for arg in ["n", "x", "p"]:
        if argMap.get(arg) is None:
            valid = False
            print(f"\tMissing -{arg} argument")
    return valid


def showHelp():
    print("A binomial distribution with n trials, x successes, and a probability of success p")


def binDist(x: int, n: int, p: float):
    """
    Compute and display probabilities using a binomial distribution
    :param x: The number of successes
    :param n: The total number of trials
    :param p: The probability of a success
    :return:
    """
    if x > n:
        raise ValueError(f"Number of successes, X = {x}, cannot exceed the number of trials, n = {n}")
    if p < 0.0 or p > 1.0:
        raise ValueError(f"Probability({p}) must be [0,1]")

    print(f"Binomial distribution with {x} successes from {n} trials and a p(x) = {p}:")

    pmf = probabilityCommon.choose(n, x) * pow(p, x) * pow(1.0 - p, n - x)
    cdf = pmf
    for i in range(0, int (x)):
        cdf += probabilityCommon.choose(n, i) * pow(p, i) * pow(1.0 - p, n - i)

    print(f"-----PMF(X={x}):\t{pmf}")
    print(f"-----CDF(X<={x}):\t{cdf}")
