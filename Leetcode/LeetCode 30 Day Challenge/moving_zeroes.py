"""
Sample
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

def move_zero(nums):
    p1 = 0
    p2 = 0
    for p1 in range(len(nums)):
        temp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = temp

        if nums[p2] != 0:
            p2 += 1
    return nums




# def move_zero(nums):
#     nums_copy = []
#     count = 0
#     if len(nums) < 2:
#         return nums
#     for i, value in enumerate(nums):
#         if value != 0:
#             nums_copy.insert(0, value)
#         else:
#             count += 1
#     if count > 0:
#         for j in range(count):
#             nums_copy.insert(0,0)
#     return nums_copy[::-1]

print(move_zero([0,1,0,3,12]))



