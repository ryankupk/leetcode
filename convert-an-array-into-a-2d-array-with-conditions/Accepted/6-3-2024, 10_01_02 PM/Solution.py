// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:
    def findMatrix(self, nums: list[int]) -> List[List[int]]:
        matrix = [[]]
        while nums:
            for num in nums[::-1]:
                if num not in matrix[-1]:
                    matrix[-1].append(num)
                    nums.remove(num)
            if nums:
                matrix.append([])
        return matrix
            
        