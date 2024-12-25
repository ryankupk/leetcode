from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        counts = Counter(arr)
        cur_to_k = 0
        for string in arr:
            if counts[string] == 1:
                cur_to_k += 1
                if cur_to_k == k:
                    return string
        
        return ""
