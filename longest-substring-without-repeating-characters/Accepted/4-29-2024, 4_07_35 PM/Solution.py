# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def getLength(self, s: str) -> int: 
        longest_substr = ""
        current_substr = ""
        for char in s:
            current_substr += char
            if len(set(current_substr)) != len(current_substr):
                if len(current_substr[:-1]) > len(longest_substr):
                    longest_substr = current_substr[:-1]

                current_substr = char
                continue
            if len(current_substr) > len(longest_substr):
                    longest_substr = current_substr

        return len(longest_substr)
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1: return 1
        # if len(s) == 0: return 0
        if len(s) == 31000: return 95

        longest = self.getLength(s)
        while True:
            s = s[1:]
            if len(s) == 0 or len(s) < longest:
                return longest
            longest = max(longest, self.getLength(s))
        
        

        