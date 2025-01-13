from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return max(Counter(s).values()) == min(Counter(s).values())
