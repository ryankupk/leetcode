# https://leetcode.com/problems/minimum-bit-flips-to-convert-number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum((1 for letter in bin(start ^ goal)[2:] if letter == '1'))