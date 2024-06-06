// https://leetcode.com/problems/strictly-palindromic-number

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return ''.join(digits[::-1])
        for i in range(2, n-1):
            if numberToBase(n, i) != numberToBase(n, i)[::-1]:
                return False
        
        return True