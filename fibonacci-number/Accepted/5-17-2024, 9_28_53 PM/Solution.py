// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        fib = [1] * n

        for i in range(2, n):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n-1]