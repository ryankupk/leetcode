from collections import Counter
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return any([i in {2 * i for i in arr} for i in arr if i != 0]) or Counter(arr)[0] >= 2
