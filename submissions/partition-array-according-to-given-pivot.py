# https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        
        less_idx = 0
        
        for num in nums:
            if num < pivot:
                result.insert(less_idx, num)
                less_idx += 1

            elif num == pivot:
                result.insert(less_idx, num)
            
            elif num > pivot:
                result.append(num)

        return result
                
            
        