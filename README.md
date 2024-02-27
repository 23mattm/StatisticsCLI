# StatisticsCLI
A command-line tool to speed up statistics grunt work.

Command guide:
## statistics.py
Run `$ python statistics.py a,b,c,d,...` where
the second argument `a,b,c,d,...` is a list of
comma-separated numbers to see statistics about
a set of data. This includes the sorted set,
the length of the set, the set's mean and median
values, the set's variance, and its standard deviation.


## probability.py
Run `$ python probability.py -dist ...` where `-dist`
is the distribution specifier and `...` is a list of
the required arguments for the given distribution.
For example, `$ python probability.py -bin -x 5 -n 10 -p 0.5`
will show data for a binomial distribution with X=5 successes,
n=10 trials, and a success probability of p=0.5

Running `$ python probability.py -h` will display
a list of all the distribution tags, and running
`$ python probability.py -dist -h` will show more
information about what's required to run a given distribution.