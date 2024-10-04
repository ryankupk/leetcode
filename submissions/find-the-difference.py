# https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(abs(sum((ord(letter) for letter in s)) - sum((ord(letter) for letter in t))))
        