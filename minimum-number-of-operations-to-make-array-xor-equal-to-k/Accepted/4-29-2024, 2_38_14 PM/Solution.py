// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

class Solution:
    def reduce(self, function, iterable):
        it = iter(iterable)
        value = next(it)
        for element in it:
            value = function(value, element)
        return value
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(map(int, (letter for letter in bin(self.reduce(lambda x, y: x^y, nums)^k) if letter == '1')))
        count = 0
        for letter in bin(self.reduce(lambda x, y: x^y, nums)^k):
            if letter == '1': count += 1

        return count
        return len([ letter for letter in bin(reduce(lambda x, y: x^y, nums)^k) if letter == '1' ])
