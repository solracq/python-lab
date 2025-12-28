import math
print(divmod(7, 2))

print(divmod(12345, 10000))
print(divmod(12345, 1000))
print(divmod(12345, 100))
print(divmod(12345, 10))

num = 12345
nums = []
size = round(math.log10(num) + 1)
for i in range(size):
    div, res = divmod(num, 10)
    nums.append(res)
    num = div
print([nums[i] for i in range(size-1, -1, -1)])