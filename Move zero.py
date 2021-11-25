def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    h = len(nums)
    for i in range(h):
        if nums[i] != 0 :
            nums[i],nums[l] = nums[l],nums[i]
            l += 1
    return nums

"""
   if i < n:
       A[n], A[i:n] = A[i], A[i+1:n+1]
    else:
       A[n], A[n+1:i+1] = A[i], A[n:i]
"""
a1 = [0,1,0,3,12]
#Output: [1,3,12,0,0]

a2 = [0]
#Output: [0]
print(moveZeroes(a1))
"""
light !
result 
Runtime: 152 ms, faster than 99.29% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 70.30% of Python3 online submissions for Move Zeroes.
"""