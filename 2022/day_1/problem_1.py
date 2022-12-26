cur_highest = 0
cur_cals = 0

with open("input_1.txt", 'r') as f:
    for line in f.readlines():
        try:
            cur_cals += int(line)
        except:
            cur_highest = max(cur_cals, cur_highest)
            cur_cals = 0

print(cur_highest)
