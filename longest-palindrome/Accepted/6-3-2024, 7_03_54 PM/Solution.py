// https://leetcode.com/problems/longest-palindrome

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        
        counts = Counter(s)
        print(counts)
        # sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_counts)
        length = 0
        remainder = 0
        for _, count in counts.items():
            if count >= 2:
                length += count - (count % 2)
                remainder += count % 2
            else:
                print(f"count < 2 and {count=}")
                remainder += count
                
        if length % 2 == 0 and remainder > 0:
            length += 1
        
        return length
                
                

        