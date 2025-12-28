'''
@author: Solrac
'''
def find_closest_sum(nums, x):
    diff = 10000000
    s = 0
    e = len(nums) - 1
    res_s = 0
    res_e = 0
    while s < e:
        if abs(nums[s] + nums[e] - x) < diff:
            res_s = s
            res_e = e
            diff = abs(nums[s] + nums[e] - x)
        if nums[s] + nums[e] < x:
            s += 1
        else:
            e -= 1
    return [res_s, res_e]

nums = [1, 3, 4, 7, 10]
x = 15
print(nums)
print(find_closest_sum(nums, x))
arr = [-1, 3, 2, -5, 4]
print(f"new : {find_closest_sum(arr, 0)}")