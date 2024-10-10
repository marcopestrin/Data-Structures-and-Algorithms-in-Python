import random

in_list = list(range(1000))
out_list = list(range(1000))
random.shuffle(in_list)

tests = []

tests.append({
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
})

tests.append({
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
})

tests.append({
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
})

tests.append({
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
})

tests.append({
    'input': {
        'nums': []
    },
    'output': []
})

tests.append({
    'input': {
        'nums': [23]
    },
    'output': [23]
})

tests.append({
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
})

tests.append({
    'input': {
        'nums': in_list
    },
    'output': out_list
})