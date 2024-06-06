# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([word for word in s.split(' ') if word != ''][-1])