class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x == 0 or x <= -2 ** 31 or x >= (2 ** 31) - 1:
            return 0
        elif x < 0:
            flag = True
            x = abs(x)
        result = [int(a) for a in str(x)]
        result = result[::-1]
        if flag:
            result.insert(0, '-')
        result1 = [str(b) for b in result]
        result1 = int(''.join(result1))
        #print(int(result1))
        return 0 if result1 >= (2 ** 31)-1 or result1 <= -(2 **31) else result1


num = 1534236469
sol = Solution()
result = sol.reverse(num)
print(result)