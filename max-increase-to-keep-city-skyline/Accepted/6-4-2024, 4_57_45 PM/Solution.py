# https://leetcode.com/problems/max-increase-to-keep-city-skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total_can_add = 0
        east_west = []
        for row in grid:
            east_west.append(max(row))

        north_south = []
        for i in range(len(grid[0])):
            col = [row[i] for row in grid]
            north_south.append(max(col))
        
        # print(f"{east_west=}")
        # print(f"{north_south=}")
        # return 0
            
        for x, row in enumerate(grid):
            for y, num in enumerate(row):
                total_can_add += abs(min(east_west[x], north_south[y]) - num)
        
        return total_can_add
                
            
        