from collections import Counter

sum_count = Counter()

class Solution:
    def isHappy(self, n):
        if n == 1:
            # print(n)
            return True
        elif sum_count[n] > 1:
            # print(n)
            return False
        else:
            nums_list = [int(x) for x in str(n)]
            # if len(nums_list) == 1 and nums_list[0] < 2:
            #     return False
            # else:
            sum = 0
            for i in nums_list:
                sum += i ** 2
            if sum == 1:
                print(sum_count)
                return True
            else:
                sum_count[sum] += 1
                return self.isHappy(sum)

num = 13
sol = Solution()
print(sol.isHappy(num))