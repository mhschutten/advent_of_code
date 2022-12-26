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


def determine_move(opp_move, expected_outcome):
    if (opp_move == 'A' and expected_outcome == 'Y') or \
            (opp_move == 'B' and expected_outcome == 'X') or \
            (opp_move == 'C' and expected_outcome == 'Z'):
        return 'X'

    if (opp_move == 'A' and expected_outcome == 'Z') or \
            (opp_move == 'B' and expected_outcome == 'Y') or \
            (opp_move == 'C' and expected_outcome == 'X'):
        return 'Y'

#    if (opp_move == 'X' and expected_outcome == 'Y')
    return 'Z'


total_score = 0
with open('input_1.txt', 'r') as f:

    for round in f.readlines():
        opp_move = round[0]
        my_move = determine_move(opp_move, round[2])

        total_score += scores[opp_move][my_move]

print(total_score)
