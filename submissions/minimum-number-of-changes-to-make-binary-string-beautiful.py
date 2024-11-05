class Solution:
    def minChanges(self, s: str) -> int:
        return sum(1 for i in range(0, len(s), 2) if s[i:i+2] == "01" or s[i:i+2] == "10")
