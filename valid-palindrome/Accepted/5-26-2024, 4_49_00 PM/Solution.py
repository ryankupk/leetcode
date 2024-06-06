# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [letter.lower() for letter in s if letter.isalnum()]
        return s == s[::-1]