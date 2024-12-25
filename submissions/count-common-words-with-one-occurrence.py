from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len(set({k: v for k, v in Counter(words1).items() if v == 1}.keys()).intersection(set({k: v for k, v in Counter(words2).items() if v == 1}.keys())))
