"""
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""
import copy
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            temp = copy.copy(nums)
            count = 0
            temp.remove(nums[i])
            for j in range(len(temp)):
                if temp[j] < nums[i]:
                    count += 1
            result.append(count)
        return result

input = [8,1,2,2,3]
sol = Solution()
result = sol.smallerNumbersThanCurrent(input)
print(result)