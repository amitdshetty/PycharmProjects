"""
Ex1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Ex2.
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Ex3.
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
"""

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(arr)):
            if (arr[i] + 1) in arr:
                count += 1
        return count

list = [1,3,2,3,5,0]
sol = Solution()
print(sol.countElements(list))
