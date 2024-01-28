# Contains mean, median
# and tests for all functions
import math
from compute import add


def summarize(sample: list):
    print('----------')
    sample.sort()
    print("Sorted set: " + str(sample) + '\n')
    print(f"Length: {len(sample)}, Min: {sample[0]}, Max: {sample[len(sample) - 1]}")
    print(f"Set sum: {add(sample)}")
    print(f"Mean: {mean(sample)}, Median: {median(sample)}")
    print(f"Set variance: {variance(sample)}, Standard Deviation: {math.sqrt(variance(sample))}")
    print('----------')


def mean(sample: list):
    s = 0
    for val in sample:
        s += val

    return s / len(sample)


def median(sample: list, trim=0.0):
    sample.sort()
    length = len(sample)

    if length % 2 == 1:
        # it's odd length set
        return sample[math.floor(length / 2)]
    else:
        # it's even length
        return (sample[math.floor(length / 2)] +
                sample[math.floor(length / 2) - 1]) / 2


def variance(sample: list):
    """
    Returns the variance of a set, calculated by the sum of squares -
    the (square of sums / n)     all over n - 1, where n is the length of the sample
    :param sample: A sample of numbers
    :return: The variance
    """
    if len(sample) < 2:
        raise IOError("Cannot calculate variance on a sample with less than 2 points")

    var = 0
    sampleMean = mean(sample)

    for val in sample:
        var += math.pow((val - sampleMean), 2.0)

    return var / (len(sample) - 1)


def sumOfSquares(numbers: list):
    sum = 0
    for num in numbers:
        sum += math.pow(num, 2)
    return sum


def test():
    print("Testing mean...")
    print("Test 1: " + str(mean([1, 2, 3, 4, 5]) == 3))
    print("Test 2: " + str(mean([1]) == 1))
    print("Test 3: " + str(mean([5, 5, 5, 10, 5]) == 6))
    print("Testing median...")
    print("Test 1: " + str(median([1, 2, 3, 4, 5]) == 3))
    print("Test 2: " + str(median([1]) == 1))
    print("Test 3: " + str(median([5, 5, 10, 5]) == 7.5))
    print("Testing variance...")
    print("Test 1: " + str(variance([10, 120, 1241, 132508])))
    print("Test 2: " + str(variance([1, 2]) == 1))
    print("Test 3: " + str(variance([5, 5, 10, 5]) == 7.5))


if __name__ == "__main__":
    test()
