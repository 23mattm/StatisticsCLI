

def factorial(n: int) -> int:
    """
    Get the factorial of a non-negative integer n
    :param n: A non-negative integer
    :return: n!
    """
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("Factorial of negative integers is undefined")
    return n * factorial(n-1)


def choose(n: int, r: int) -> float:
    """
    Get the value of the combination n choose r, where r <= n
    :param n: The total sample size
    :param r: The amount of items to choose
    :return: C(n, r)
    """
    if r > n:
        raise ValueError(f"Cannot choose {r} items from {n} total")

    return factorial(n) / (factorial(r) * factorial(n - r))


def displayStats(x, pmf, cdf, discrete=True):
    print(f"---PMF(X={x}):\t\t{pmf}")
    if discrete:
        print(f"---CDF(X<={x}):\t\t{cdf}")
        print(f"---CDF(X<{x}): \t\t{cdf - pmf}")
        print(f"---CDF(X>={x}):\t\t{1.0 - (cdf - pmf)}")
        print(f"---CDF(X>{x}): \t\t{1.0 - cdf}")
    else:
        print("---This distribution is continuous; continuous cdf is WIP")
        print(f"---To find the cdf X<={x}, take the integral of the pdf from -infinity to {x}")
    print()

