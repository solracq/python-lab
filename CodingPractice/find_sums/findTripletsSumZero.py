'''
@author: Solrac
'''
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
def triplets_sum_zero(nums):
    nums.sort()
    found = False
    for i in range(0, len(nums)-1):
        s = i + 1
        e = len(nums) - 1
        while s < e:
            if nums[s] + nums[e] + nums[i] == 0:
                print(f"indexes: {s}, {e}, {i}")
                print(f"Nums: {nums[s]}, {nums[e]}, {nums[i]}")
                found = True
                s += 1
                e -= 1
            elif nums[s] + nums[e] + nums[i] < 0:
                s += 1
            else:
                e -= 1
    return found

nums = [0, -1, 2, -3, 1]
print(sorted(nums))
print(triplets_sum_zero(nums))
 