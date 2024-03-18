from math import pow, gamma, e
from ProbabilityTools.probabilityCommon import displayStats


def validArgs(argMap: dict) -> bool:
    valid = True
    for arg in ["x", "a", "b"]:
        if argMap.get(arg) is None:
            valid = False
            print(f"\tMissing -{arg} argument")

    return valid


def showHelp():
    print("A Weibull distribution with rv X=x, and parameters alpha = a, beta = b\n")
    print("Required arguments:")
    print("---x: the random variable X")
    print("---a: the alpha parameter")
    print("---b: the beta parameter")
    print()
    print("Try running:\n\tpython probability.py -weib -x 1 -a 3 -b 5\n")


def findpdf(x: float, alpha: float, beta: float) -> float:
    return (alpha / pow(beta, alpha)) * pow(x, alpha-1) * pow(e, -pow(x/beta, alpha))


def findcdf(x: float, alpha: float, beta: float) -> float:
    return 1 - pow(e, -pow(x/beta, alpha))


def findmean(alpha: float, beta: float) -> float:
    return beta * gamma(1 + (1/alpha))


def findvar(alpha: float, beta: float) -> float:
    return pow(beta, 2) * (gamma(1 + (2/alpha)) - pow(gamma(1+(1/alpha)), 2))


def weibull(x: float, alpha: float, beta: float):

    pdf = findpdf(x, alpha, beta)
    cdf = findcdf(x, alpha, beta)

    mean = findmean(alpha, beta)
    variance = findvar(alpha, beta)

    displayStats(
        x,
        pdf,
        cdf,
        mean,
        variance,
        False
    )




