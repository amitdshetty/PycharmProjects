class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {}
        for i, value in enumerate(strs):
            print(value)
            result_dict.setdefault(''.join(sorted(value)), []).append(value)
        return list(result_dict.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(words))
