// https://leetcode.com/problems/ugly-number

class Solution:
    def prime_factors(self, n):
        factors = []
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            factors.append(n)
        return factors

    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0: return False

        for factor in self.prime_factors(n):
            if factor not in [2, 3, 5]:
                return False
        return True