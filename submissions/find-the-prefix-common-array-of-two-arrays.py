class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return [len(set(A[:i+1]).intersection(set(B[:i+1]))) for i, _ in enumerate(A)]
