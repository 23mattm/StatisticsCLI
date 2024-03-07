from math import e, pi, sqrt, pow
from ProbabilityTools.probabilityCommon import displayStats


def validArgs(argMap: dict) -> bool:
    valid = True
    for arg in ["x", "u", "o"]:
        if argMap.get(arg) is None:
            valid = False
            print(f"\tMissing -{arg} argument")

    return valid


def showHelp():
    print("A Normal distribution with mean u, rv X=x, and a standard deviation o\n")
    print("Required arguments:")
    print("---x: the random variable X")
    print("---u: the mean of the distribution(0 in a standard normal)")
    print("---o: the standard deviation of the distribution(1 in a standard normal)")
    print()
    print("Try running:\n\tpython probability.py -norm -x 1 -u 3 -o 5\n")


def normalDist(x: float, u: float, o: float):
    """
    Compute a normal distribution with X=x, mean u, and standard deviation o
    :param x: The random variable x
    :param u: The mean (center) of the distribution
    :param o: The standard deviation of the distribution
    :return:
    """
    pdf = (1.0 / (o * sqrt(2*pi))) * pow(e, -pow(x-u, 2)/pow(2*o, 2))
    cdf = pdf

    displayStats(x, pdf, cdf, u, pow(o, 2))


