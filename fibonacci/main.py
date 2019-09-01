#!/usr/bin/env
import argparse

parser = argparse.ArgumentParser(description='How many fibonacci do you want.')
parser.add_argument('--number', default='10', type=int, help='an int')

args = parser.parse_args()
n = args.number

# F(n) = F(n-1) + F(n-2) // with F(0) = 0 and F(1) = 1
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

for index, fibonacciNum in zip(range(n), fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacciNum))
