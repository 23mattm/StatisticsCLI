from ProbabilityTools import (
    binomialDistribution, poisson, normalDistribution)
import sys


def showHelp():
    print("Please specify a probability distribution from the list below:")
    print()
    print("\t-bin\t a binomial distribution(requires -x, -n, -p).")
    print("\t-pois\t a poisson distribution(requires -x, -u).")
    print("\t-norm\t a normal distribution(requires -x, -u, -o).")


def parseArgs(arguments: list) -> dict:
    """
    Parse program arguments into a dictionary.
    :param arguments: A list of the program arguments
    (excluding the program path and the distribution instruction)
    :return:A dictionary mapping all - arguments to the following string
    """
    result = dict()

    while len(arguments) > 0:
        param = arguments.pop(0)
        if param[0] == "-":
            if param[1:] == "h":  # If the help tag is spotted, no other arguments matter
                result["h"] = 0
                break

            value = arguments.pop(0)
            if value.find("."):
                value = float(value)
            else:
                value = int(value)

            result[param[1:]] = value
        else:
            raise IOError("Arguments not formatted correctly. Format arguments as \'-arg1 val1 -arg2 val2\'")

    return result


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 2:
        raise IOError("Missing arguments. Use -h to see a complete list")

    print("------------")
    if args[1] == "-h":
        showHelp()
        sys.exit(0)

    argMap = parseArgs(args[2:])

    helpTag = not (argMap.get("h") is None)

    if args[1] == "-bin":
        if helpTag:
            binomialDistribution.showHelp()
        else:
            if binomialDistribution.validArgs(argMap):
                binomialDistribution.binDist(
                    argMap.get("x"),
                    argMap.get("n"),
                    argMap.get("p")
                )
    elif args[1] == "-pois":
        if helpTag:
            poisson.showHelp()
        else:
            if poisson.validArgs(argMap):
                poisson.poisson(
                    argMap.get("x"),
                    argMap.get("u")
                )
    elif args[1] == "-norm":
        if helpTag:
            normalDistribution.showHelp()
        else:
            if normalDistribution.validArgs(argMap):
                normalDistribution.normalDist(
                    argMap.get("x"),
                    argMap.get("u"),
                    argMap.get("o")
                )
    else:
        print("No distribution specified.")
        showHelp()


    print("------------")