import string

prio = {char: prio for prio, char in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)}

prio_sum = 0
with open('input.txt', 'r') as f:
    for line_nr, rugsack in enumerate(f.readlines()):

        # Readlines counts the newline for all lines, except the last
        num_items = int(len(rugsack) / 2)

        compartment_1 = set(rugsack[:num_items])
        compartment_2 = set(rugsack[num_items:-1])

        prio_sum += prio[list(compartment_1.intersection(compartment_2))[0]]

print(prio_sum)
