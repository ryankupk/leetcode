# https://leetcode.com/problems/rearrange-characters-to-make-target-string

from collections import Counter
from math import floor

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(set(target).difference(set(s))) > 0: return 0
        new_s = [letter for letter in s if letter in target]
        s_counts = Counter(new_s)
        target_counts = Counter(target)
        min_possible = float('inf')
        for s_char, s_count in s_counts.items():
            # if s_char not in target: continue
            if not s_count >= target_counts[s_char]: return 0
            else: 
                min_possible = floor(s_count // target_counts[s_char]) if floor(s_count // target_counts[s_char]) < min_possible else min_possible
        return min_possible
        # return min([count for char, count in s_counts.items() if char in target]) if len(set(target)) == len(target)


"""
{
    a: 2,
    b: 2,
    c: 1
}
"""