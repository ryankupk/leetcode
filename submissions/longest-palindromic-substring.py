# https://leetcode.com/problems/longest-palindromic-substring

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(Counter(s)) == 1:
            return s
        
        def is_palindrome(string: str):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        longest = ""
        for i, char in enumerate(s):
            for j in range(i+1, len(s)+1):
                # print(f"{i=}")
                # print(f"{j=}")
                # print(f"{s[i:j]=}")
                if is_palindrome(s[i:j]) and len(s[i:j]) > len(longest):
                    longest = s[i:j]

        return longest
        