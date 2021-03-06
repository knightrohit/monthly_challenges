"""
Time/Space complexity = O(1)
"""
import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        if not num or num < 0:
            return False

        val = math.log(num, 4)
        return not(val > int(val))


# Using bitwise operator
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (-num) == num and num & 0xaaaaaaaa == 0