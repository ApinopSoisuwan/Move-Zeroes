def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    c = nums.count(0)
    while 0 in nums:
        nums.remove(0)
    for i in range(c):
        nums.append(0)
    return nums
a1 = [0,1,0,3,12]
#Output: [1,3,12,0,0]

a2 = [0]
#Output: [0]
print(moveZeroes(a1))
"""
heavy load
result 
Runtime: 968 ms, faster than 11.08% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.7 MB, less than 10.06% of Python3 online submissions for Move Zeroes. 
"""