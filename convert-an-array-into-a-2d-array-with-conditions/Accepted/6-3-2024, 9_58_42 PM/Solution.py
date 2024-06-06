# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:
    def findMatrix(self, nums: list[int]) -> List[List[int]]:
        matrix = [[]]
        row = 0
        while nums:
            for num in nums[::-1]:
                if num not in matrix[row]:
                    matrix[row].append(num)
                    nums.remove(num)
            matrix.append([])
            row += 1
        return matrix[:-1]
            
        