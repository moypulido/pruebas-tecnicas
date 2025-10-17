# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 


def two_sum(list: list[int], target: int) -> list[int]:
    
    if len(list) < 1:
        return None
    
    hash_map = {} 
    
    for i, n in enumerate(list):
        need = target - n
        if need in hash_map:
            return [hash_map[need], i]
        hash_map[n] = i 

    return None

print(two_sum([2,5,6,7,10], 7))
