import fileinput

from math import floor

lines = iter(fileinput.input())

n, k = [int(i) for i in next(lines).split()]

print((floor(n / k) + 1) * k)
