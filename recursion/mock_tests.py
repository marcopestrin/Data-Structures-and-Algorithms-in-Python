tests = []
tests.append({
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
})

tests.append({
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
})

tests.append({
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
})

tests.append({
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
})

tests.append({
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
})

tests.append({
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
})

tests.append({
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
})

tests.append({
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
})