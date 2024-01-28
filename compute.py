from summarizeData import *
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
        raise IOError("Set not inputted correctly")


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
            numbers = parseToSet(args[2])

            print("Set: " + str(numbers))
            if command == 'summarize':
                summarize(numbers)
            elif command == 'mean':
                print("Mean: " + str(mean(numbers)))
            elif command == 'median':
                print("Median: " + str(median(numbers)))
            elif command == 'add':
                print("Sum: " + str(add(numbers)))
            elif command == 'sumsquares':
                print("Sum of squares: " + str(sumOfSquares(numbers)))
    else:
        print("add arguments")
