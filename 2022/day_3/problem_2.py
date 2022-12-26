import string

prio = {char: prio for prio, char in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)}

prio_sum = 0
with open('input.txt', 'r') as f:
    for line_nr, rugsack in enumerate(f.readlines()):

        if line_nr % 3 == 0:
            potential_unique_items = set(rugsack[:-1])

        potential_unique_items = potential_unique_items.intersection(set(rugsack))

        if line_nr % 3 == 2:
            prio_sum += prio[list(potential_unique_items)[0]]

print(prio_sum)
