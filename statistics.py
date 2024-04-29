from StatisticsTools import summarizeData
import sys

if __name__ == "__main__":
    args = sys.argv
    print(args)

    if (len(args) == 1):
        print("No set provided! The second argument should be a list of comma\
-separated numbers(i.e 1,2,3,4,5)")
        sys.exit(1)

    numbers = list()

    for num in args[1].split(" "):
        if num.find("."):
            num = float(num)
        else:
            num = int(num)

        numbers.append(num)

    summarizeData.summarize(numbers)
