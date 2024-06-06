// https://leetcode.com/problems/max-increase-to-keep-city-skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total_can_add = 0
        # east_west = []
        # for row in grid:
        #     east_west.append(max(row))

        # north_south = []
        # for i in range(len(grid[0])):
        #     col = [row[i] for row in grid]
        #     north_south.append(max(col))
        
        for x, row in enumerate(grid):
            east_west = max(row)
            # print(f"{east_west=}")
            for y, num in enumerate(row):
                north_south = max([r[y] for r in grid])
                # print(f"{north_south=}")
                total_can_add += abs(min(east_west, north_south) - num)
        
        return total_can_add
                
            
        