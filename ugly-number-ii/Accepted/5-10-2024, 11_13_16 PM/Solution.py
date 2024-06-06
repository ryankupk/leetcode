// https://leetcode.com/problems/ugly-number-ii

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

    def isUgly(self, n: int, uglies: List[int]) -> bool:
        if n == 1: return True
        if n <= 0: return False

        for ugly in uglies:
            if n == 2 * ugly or n == 3 * ugly or n == 5 * ugly:
                return True

        for factor in self.prime_factors(n):
            if factor not in [2, 3, 5]:
                return False
        return True

    def generateUglies(self):
        n = 1690
        uglies = [1]
        for i in range(1, n):
            if self.isUgly(i, uglies):
                for factor in [2, 3, 5]:
                    uglies.append(i * factor)
        
        return sorted(list(set(uglies)))

    def nthUglyNumber(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        uglies = [0] * (n)
        i2, i3, i5 = 0, 0, 0
        next_2 = 2
        next_3 = 3
        next_5 = 5

        for i in range(1, n):
            uglies[i] = min(next_2, next_3, next_5)

            if uglies[i] == next_2:
                i2 += 1
                next_2 = uglies[i2] * 2
            if uglies[i] == next_3:
                i3 += 1
                next_3 = uglies[i3] * 3
            if uglies[i] == next_5:
                i5 += 1
                next_5 = uglies[i5] * 5
        return uglies[-1]

        # print(self.generateUglies())
        return self.generateUglies()[n-1]
        uglies = []
        current = 1
        while len(uglies) < n:
            if self.isUgly(current, uglies):
                print(f"{current} is ugly")
                uglies.append(current)
            current += 1
        
        return uglies[-1]