from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def count_rotations(nums):
    # binary search
    # big o notation --> O(log N)
    lo, hi = 0, len(nums)-1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if mid < hi and nums[mid] > nums[mid + 1]:
            return mid + 1
        if mid > lo and nums[mid] < nums[mid - 1]:
            return mid
        if nums[mid] > nums[lo]:
            # right side
            lo = mid + 1
        else:
            # left side
            hi = mid - 1

    return 0


evaluate_test_cases(count_rotations, tests)
