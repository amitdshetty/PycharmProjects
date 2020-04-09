"""
Works only for addition not subtraction

"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        mask = 0xfffffff
        i = 0
        while b != 0:
            i += 1
            a = (a ^ b) & mask
            b = ((a & b) << 1) & mask
        print(i)
        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

# class Solution(object):
#     def getSum(self, a, b):
#         """
#         :type a: int
#         :type b: int
#         :rtype: int
#         """
#         # The number determines how much
#         a = '{0:07b}'.format(abs(a))
#         b = '{0:07b}'.format(abs(b))
#         # [a, b] ==> ('0001100', '0001000')
#         # print(a, b)
#         result = []
#         carry  = 0
#         # print("before {}, {}".format(a, b))
#         a, b = a[::-1], b[::-1]
#         print("after {}, {}".format(a, b))
#         for x, y in zip(a, b):
#             if x == y:
#                 result.insert(0, 0 + carry)
#                 if carry == 1:
#                     carry = 0
#                 if int(x) == 1 or int(y) == 1:
#                     carry = 1
#             else:
#                 z = carry + int(x) + int(y)
#                 if z == 2:
#                     carry = 1
#                     z = 0
#                 # Reset carry back to 0 once done
#                 # carry = 0
#                 result.insert(0, z)
#         if carry == 1:
#             result.insert(0, 1)
#         print(result)
#         # Convert binary to decimal
#         dec_result = 0
#         for i, x in enumerate(result[::-1]):
#             if x == 1:
#                 dec_result += 2 ** i
#         return dec_result



a, b = 50, -8
sol = Solution()
c = sol.getSum(a, b)
print("Result is ", c)