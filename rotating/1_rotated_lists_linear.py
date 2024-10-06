from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def count_rotations(nums):
    # linear search
    # big o notation --> O(n)
    position = 1
    while position < len(nums):
        if nums[position] < nums[position-1]:
            return position
        position += 1
    return 0

evaluate_test_cases(count_rotations, tests)
