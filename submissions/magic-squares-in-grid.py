# https://leetcode.com/problems/magic-squares-in-grid



"""
[
    [4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]
]
"""

from collections import defaultdict

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        width, height = 3, 3
        target = 15
        magic_count = 0
        if len(grid) < height or len(grid[0]) < width: # must have at least one 3x3 grid
            return 0

        def subgrid_contains_nums(subgrid: list[list[int]]):
            counts = defaultdict(int)
            for row in subgrid:
                for num in row:
                    if num > 9 or num < 1:
                        print(f"num out of bounds: {num}")
                        return False
                    counts[num] += 1
                    if counts[num] > 1:
                        print(f"num count too high: {num}")
                        return False
            return True
            
        def subgrid_meets_target(subgrid: list[list[int]]):
            for row in subgrid:
                if sum(row) != target:
                    print("row sum doesn't meet target")
                    return False

            for col in zip(*subgrid):
                print(col)
                if sum(col) != target:
                    print("col sum doesn't meet target")
                    return False
            
            top_left_diagonal = 0
            top_left_diagonal += subgrid[0][0]
            top_left_diagonal += subgrid[1][1]
            top_left_diagonal += subgrid[2][2]
            if top_left_diagonal != target:
                print("top left diagonal doesn't meet target")
                return False

            top_right_diagonal = 0
            top_right_diagonal += subgrid[0][0]
            top_right_diagonal += subgrid[1][1]
            top_right_diagonal += subgrid[2][2]
            if top_right_diagonal != target:
                print("top right diagonal doesn't meet target")
                return False

            return True
            

        for x in range(len(grid[0])-width+1):
            for y in range(len(grid)-height+1):
                subgrid = []
                for i in range(height):
                    subgrid.append(grid[y+i][x:x+width])
                
                print(subgrid_contains_nums(subgrid))
                if subgrid_contains_nums(subgrid) and subgrid_meets_target(subgrid):
                    magic_count += 1
        
        return magic_count
            
        