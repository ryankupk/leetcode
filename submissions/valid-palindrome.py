# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [letter.lower() for letter in s if letter.isalpha() or letter.isdigit()]
        print(f"{s=}")
        return s == s[::-1]