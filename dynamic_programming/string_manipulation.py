import time

str1 = "intention"
str2 = "execution"
## should be 5

str3 = "monday"
str4 = "saturday"
## should be 5

str5 = "abc"
str6 = "xyz"
## should be 3

str7 = "metropoli"
str8 = "megalopoli"
## should be 3

str9 = "oil"
str10 = "boiler"
## should be 3

str11 = "induism"
str12 = "buddhism"
## should be 4

def min_step(str1, str2, idx1=0, idx2=0):

    # print(" "*idx1, "str1:", str1[idx1:], " str2:",str2[idx2:])

    if len(str1) == idx1:
        # print("len(str2):", len(str2), " idx2:", idx2)
        return len(str2) - idx2
    
    if len(str2) == idx2:
        # print("len(str1):", len(str1), " idx1:", idx1)
        return len(str1) - idx1
    
    if str1[idx1] == str2[idx2]:
        # if char is equal ignore then ignore from both
        # now we want to recursively solve the problem but with the next char
        return min_step(str1, str2, idx1+1, idx2+1)

    # recursion is very usefull you can simply use your function to solve some problems
    # and then combine the subproblem to resolve the main one
    
    # option1:
    # delete the first character of str1 skipping ahead into the next one
    # because we are solving now the problem starting from next index
    # this mean delete the character
    opt1 = min_step(str1, str2, idx1+1, idx2)

    # option2:
    # swapped/replaced the character
    opt2 = min_step(str1, str2, idx1+1, idx2+1)

    # option3:
    # inserted a new character before
    opt3 = min_step(str1, str2, idx1, idx2+1)

    # select the solution with minimum steps.
    # pick the minimum one
    return 1+min(opt1, opt2, opt3)


def min_edit_distance_memo(str1, str2):
    # initialization empty dictionary to store repeated cases
    memo = {}

    def recurse(i1, i2):
        key = i1, i2
        if key in memo:
            # save into dictionary 
            return memo[key]
        elif i1 == len(str1):
            # move the selector
            memo[key] = len(str2)-i2
        elif i2 == len(str2):
            # move the selector
            memo[key] = len(str1)-i1
        elif str1[i1] == str2[i2]:
            # character are equal.
            # go to next one
            memo[key] = recurse(i1+1, i2+1)
        else:
            # pick the minimum path to resolve
            memo[key] = 1+min(recurse(i1+1, i2),
                              recurse(i1+1, i2+1),
                              recurse(i1, i2+1))
        return memo[key]
    
    return recurse(0,0)

start_time = time.time()
print(min_step(str1, str2))
print(min_step(str3, str4))
print(min_step(str5, str6))
print(min_step(str7, str8))
print(min_step(str9, str10))
print(min_step(str11, str12))
end_time = time.time()
print('time execution: ', end_time - start_time)

start_time = time.time()
print(min_edit_distance_memo(str1, str2))
print(min_edit_distance_memo(str3, str4))
print(min_edit_distance_memo(str5, str6))
print(min_edit_distance_memo(str7, str8))
print(min_edit_distance_memo(str9, str10))
print(min_edit_distance_memo(str11, str12))
end_time = time.time()
print('time execution: ', end_time - start_time)