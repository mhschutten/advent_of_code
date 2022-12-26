# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

scores = {

    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },

    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },

    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
}

total_score = 0
with open('input_1.txt', 'r') as f:
    for round in f.readlines():
        total_score += scores[round[0]][round[2]]

print(total_score)
