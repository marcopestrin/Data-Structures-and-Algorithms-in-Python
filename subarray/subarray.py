import time
start_time = time.time()

arr1 = [1, 7, 4, 2, 1, 3, 11, 5]
target1 = 10

arr2 = [7, 4, 6, 2, 2, 2]
target2 = 10

arr3 = [1, 2, 7, 9, 4, 2, 13, 2, 5]
target3 = 15

def subarray_sum1(arr, target):
    # brute force solution
    # big o notation: O(n^2)
    for i in range(0, len(arr)):
        for j in range(i, len(arr)+1):
            if sum(arr[i:j]) == target:
                return i,j
    return None, None

def subarray_sum2(arr, target):
    # big o notation: O(n)
    for i in range(len(arr)):
        s = 0 # running sum
        for j in range(i, len(arr)+1):
            if s == target:
                # found the first occurrence in the list
                return i,j
            elif s > target:
                # out of range
                # skip to next one
                break
            if j < len(arr):
                # there is a possibility to try the next sum
                s = s+arr[j]
    return None, None

def subarray_sum3(arr, target):
    i,j,s, = 0,0,0 # indexes
    while i < len(arr) and j < len(arr)+1:
        if s == target:
            return i,j
        elif s < target:
            if j < len(arr):
                s = s + arr[j]
            j = j + 1
        elif s > target:
            # first index must be increase
            # means remove the first number
            s = s - arr[i]
            i = i + 1
    return None, None

start_time = time.time()
print(subarray_sum1(arr1, target1))
print(subarray_sum1(arr2, target2))
print(subarray_sum1(arr3, target3))
end_time = time.time()
print('time execution: ', end_time - start_time)

start_time = time.time()
print(subarray_sum2(arr1, target1))
print(subarray_sum2(arr2, target2))
print(subarray_sum2(arr3, target3))
end_time = time.time()
print('time execution: ', end_time - start_time)

start_time = time.time()
print(subarray_sum3(arr1, target1))
print(subarray_sum3(arr2, target2))
print(subarray_sum3(arr3, target3))
end_time = time.time()
print('time execution: ', end_time - start_time)