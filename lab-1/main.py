import numpy as np

ddd = {'1': 1, '2': 2}

lll = [1, 2, 5, 6]
lll.sort()
print(f'LLL: {lll}')

# teams_prob = [(key, np.random.rand()) for key in ddd.keys()].sort(key=lambda x: x[1])
teams_prob = [(key, np.random.rand()) for key in ddd.keys()]
teams_prob.sort(key=lambda x: x)


print(teams_prob)

for val1, val2 in teams_prob:
    print(val1, val2)
