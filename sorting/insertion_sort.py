from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def insertion_sort(nums):
    # complexity O(n^2)
    nums = list(nums)
    for i in range(len(nums)):
        # remove an element to the list and save that element into cur
        # this change the length of nums
        cur = nums.pop(i)

        # j is the index immediately before i
        # it will be the right position for cur
        j = i-1

        # find the right position to insert cur
        # compare cur with all elements before i
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

results = evaluate_test_cases(insertion_sort, tests)
# print(results)
