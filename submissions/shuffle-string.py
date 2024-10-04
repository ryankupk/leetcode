# https://leetcode.com/problems/shuffle-string

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = [" "] * len(s)
        
        for i, char in enumerate(s):
            new_s[indices[i]] = char
            
        return ''.join(new_s)

