# O(log n)
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
from mock_tests import large_test, tests

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

evaluate_test_cases(locate_card, tests)

result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))

# Result: 9999998
# Passed: True
# Execution Time: 0.248 ms

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

print(first_and_last_position([5,7,7,8,8,10], 8)) #[3,4]
print(first_and_last_position([5,7,7,8,8,10], 6)) #[-1,-1]
print(first_and_last_position([3,5,7,7,8,8,8,8,10], 8)) #[4,7]
print(first_and_last_position([], 0)) #[-1,-1]
