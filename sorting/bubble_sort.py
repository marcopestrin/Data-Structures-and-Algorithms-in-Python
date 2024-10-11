from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def bubble_sort(nums):
    # big o notation --> O(n^2) (quadratic complexity)
    # 1. iterate over the list of numbers, starting from the left
    # 2. compare each number with the number that follows it
    # 3. if the number is greater than the one that follows it, swap the two elements
    # 4. repeat steps 1 to 3 till the list is sorted
    # 5. repeat steps 1 to 3 at most n-1 times to ensure that the array is sorted
    # 6. after one iteration, the largest number in the list

    # create a copy of the list, to avoid changing it
    nums = list(nums)
    
    # 5. repeat the process n-1 times
    for _ in range(len(nums) - 1):
        
        # 1. iterate over the array (except last element)   
        for i in range(len(nums) - 1):
            
            # 2. compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # return the sorted list
    return nums


results = evaluate_test_cases(bubble_sort, tests)
# print(results)
