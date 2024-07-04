#Statement

# We're given a sorted list, nums, containing positive integers only. We have to rearrange the list so that when returned, the 
#  index of the list will have the largest number, the first
#  index will have the smallest number, the second
#  index will have the second largest number, the third 
#  index will have the second smallest number, and so on.
# In the end, we’ll have the largest remaining numbers in descending order and the smallest in ascending order at even and odd positions, respectively

# SOLUTION

def rearrange_list(nums):
    result = []
    k = 0
    while len(result) < len(nums):
        _max = nums[-(k+1)]
        result.append(_max)
        if len(result) != len(nums):
            _min = nums[k]
            result.append(_min)
        k+=1
    
    return result