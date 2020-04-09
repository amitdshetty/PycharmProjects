import bisect
class Solution(object):
    def countSmaller(self, nums):
        counts = []
        done = []
        for num in nums[::-1]:
            # TBD Read documentation
            i = bisect.bisect_left(done, num)
            counts.insert(0, i)
            bisect.insort(done, num)
            """
            insort is basically doing the same operation what these 2 are doing below
            From the documentation it looks like performance here O(n) insertion dominates O(log n) search
            """
            # done.append(num)
            # done = sorted(done)
        return counts

# old one too slow for very large dataset
# class Solution(object):
#     def countSmaller(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         if len(nums) < 2:
#             result.append(0)
#         else:
#             for i in range(len(nums)):
#                 count = 0
#                 temp = nums[i]
#                 for j in range(i+1, len(nums)):
#                     if nums[j] < temp:
#                         count += 1
#                 result.append(count)
#         return result
#
list_nums = [5, 2, 6, 1]
sol = Solution()
result = sol.countSmaller(list_nums)
print(result)