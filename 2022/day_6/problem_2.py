with open('input.txt', 'r') as f:
    line = f.readline()

    cur_chars = line[:14]
    cur_pos = 0

    while len(set(cur_chars)) < 14:
        cur_pos += 1
        cur_chars = line[cur_pos:cur_pos + 14]

    print(cur_pos + 14)
