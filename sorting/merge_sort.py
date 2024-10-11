from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

def merge(nums1, nums2, depth=0):
    print('  '*depth, 'merge:', nums1, nums2) # only for debugging

    # List to store the results 
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):        
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts
    # one of the two will be empty
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return the final merged array
    return merged + nums1_tail + nums2_tail

def merge_sort(nums, depth=0):
    print('  '*depth, 'merge_sort:', nums) # only for debugging

    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid] # excluded mid
    right = nums[mid:] # included mid
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left, depth+1), merge_sort(right, depth+1)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted, depth+1)
    
    return sorted_nums


results = evaluate_test_cases(merge_sort, tests)
# print(results)