import fileinput

from math import gcd

lines = iter(fileinput.input())

n, a, b, p, q = [int(i) for i in next(lines).split()]

lcm = a * b // gcd(a, b)

biggest = max(p, q)

chocolates = n // a * p + n // b * q - n // lcm * (q if biggest == p else p)

print(chocolates)
