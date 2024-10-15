from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def max_profit(weights, profits, capacity, idx=0):
    if idx == len(weights):
        # no more recursion because we finish the cases
        return 0
    elif weights[idx] > capacity:
        # we simply ignore this element because there's no space in the capacity that we have
        return max_profit(weights, profits, capacity, idx+1)
    else:
        opt1 = max_profit(weights, profits, capacity, idx+1)
        # try to add this item summing this profit andsubtrack this weight from the remaining capacity
        opt2 = profits[idx] + max_profit(weights, profits, capacity-weights[idx], idx+1)
        return max(opt1, opt2)


def max_profit_dp(weights, profits, capacity):
    # dp --> dynamic programming
    n = len(weights)
    table = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    print('weights:',weights,' profits:', profits, ' capacity:', capacity)
    for i in range(n):
        # vertical row are weights
        for c in range(1, capacity+1):
            # horizontal line is the capacity
            print('__________________')
            print('weight:', weights[i],  'this profit: ', profits[i])
            opt1 = table[i][c]
            if weights[i] > c:
                # print('opt1:', opt1)
                table[i+1][c] = opt1
            else:
                opt2 = profits[i] + table[i][c-weights[i]]
                table[i+1][c] = max(opt1, opt2)
                print('--------->','weight:',weights[i],' profit opt1:', opt1, ' profit opt2:', opt2, 'selected: ',max(opt1, opt2), 'this profit: ', profits[i])
            
            for row in table:
                print(' | '.join(f'{item:2}' for item in row))
    return table[-1][-1]



evaluate_test_cases(max_profit_dp, [{
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}])
