// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacement = {}
        for s_char, t_char in zip(s, t):
            if s_char not in replacement:
                if t_char in replacement.values():
                    return False

                replacement[s_char] = t_char
                continue
            
            if replacement[s_char] != t_char:
                return False

        return True