cur_highest = [0, 0, 0]
cur_cals = 0

with open("input_1.txt", 'r') as f:
    for line in f.readlines():
        try:
            cur_cals += int(line)
        except:
            cur_highest.append(cur_cals)
            cur_highest = sorted(cur_highest, reverse=True)[:3]
            cur_cals = 0


print(sum(cur_highest))
