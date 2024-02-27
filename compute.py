import probability
# from statistics import summarizeData
# from statistics.summarizeData import *
from probability import *
import sys


def parseToSet(numbers: str) -> list:
    """
    Parse a string of space-separated numbers into a list.
    :raise IOError: If the formatting cannot be read
    :param numbers: A string of numbers separated by spaces
    :return: The numbers as a list
    """
    _l = list()
    try:
        for val in numbers.split():
            _l.append(float(val.strip()))
        return _l
    except Exception:
        raise IOError("Set not entered correctly")


def add(numbers: list):
    sum = 0
    for num in numbers:
        sum += num

    return sum


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 2:
        command = args[1]
        if command[0:2] != '--':
            raise IOError("Preface your command with --")
        else:
            command = command[2:]

            if command == 'summarize':
                numbers = parseToSet(args[2])
                summarizeData.summarize(numbers)
            elif command == 'mean':
                numbers = parseToSet(args[2])
                print("Mean: " + str(mean(numbers)))
            elif command == 'median':
                numbers = parseToSet(args[2])
                print("Median: " + str(median(numbers)))
            elif command == 'add':
                numbers = parseToSet(args[2])
                print("Sum: " + str(add(numbers)))
            elif command == 'sumsquares':
                numbers = parseToSet(args[2])
                print("Sum of squares: " + str(sumOfSquares(numbers)))
            elif command == 'expectedvalue':
                numbers = parsePMF(args[2])
                print("Expected value: " + str(expectedValue(numbers)))
            elif command == 'pmfvariance':
                numbers = parsePMF(args[2])
                print("Variance: " + str(probability.variance(numbers)))
    else:
        print("add arguments")
