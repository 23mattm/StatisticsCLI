

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
