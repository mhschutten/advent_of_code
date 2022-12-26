import re

section_division_re = re.compile(r'(?P<min_1>\d+)-(?P<max_1>\d+),(?P<min_2>\d+)-(?P<max_2>\d+)')

count = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        min_1, max_1, min_2, max_2 = (int(x) for x in section_division_re.match(line).groups())

        count += (min_2 <= min_1 <= max_2) or \
                 (min_1 <= min_2 <= max_1) or \
                 (max_2 >= max_1 >= min_2) or \
                 (max_1 >= max_2 >= min_1)

print(count)
