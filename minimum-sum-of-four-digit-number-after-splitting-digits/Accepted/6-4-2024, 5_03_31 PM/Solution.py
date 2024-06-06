# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([digit for digit in str(num)])
        return int(digits[0] + digits[3]) + int(digits[1] + digits[2])
        