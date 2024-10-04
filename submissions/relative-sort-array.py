# https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        rank_map = {value: idx for idx, value in enumerate(arr2)}

        def sort_key(x):
            return (rank_map.get(x, float('inf')), x)

        arr1.sort(key=sort_key)
        return arr1