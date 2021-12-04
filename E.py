import fileinput

lines = iter(fileinput.input())

y = int(next(lines))

is_leap_year = lambda x: (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0)

y_is_leap_year = is_leap_year(y)

day_idx = 2 if y_is_leap_year else 1
cur_yr = y + 1

while not (is_leap_year(cur_yr) == y_is_leap_year and day_idx == 0):
    if is_leap_year(cur_yr):
        day_idx += 2
    else:
        day_idx += 1
    day_idx %= 7
    cur_yr += 1

print(cur_yr)
