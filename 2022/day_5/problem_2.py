import re

state = [
    'RNPG',
    'TJBLCSVH',
    'TDBMNL',
    'RVPSB',
    'GCQSWMVH',
    'WQSCDBJ',
    'FQL',
    'WMHTDLFV',
    'LPBVMJF',
]

moves_re = re.compile(r'move (?P<n_moves>\d+) from (?P<source_stack>\d+) to (?P<target_stack>\d+)')

with open('input.txt', 'r') as f:
    for line in f.readlines():

        n_moves, source_stack, target_stack = (int(x) for x in moves_re.match(line).groups())
        source_stack -= 1
        target_stack -= 1

        stack = state[source_stack][-n_moves:]

        state[target_stack] += stack
        state[source_stack] = state[source_stack][:-n_moves]

print(''.join(stack[-1] for stack in state))
