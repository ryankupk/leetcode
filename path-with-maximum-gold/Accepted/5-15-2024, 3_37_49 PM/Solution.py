// https://leetcode.com/problems/path-with-maximum-gold

class Solution:
    def path_value(self, grid, row, col, visited):
        if ( # bounds check, skip no-value cells
           row < 0 
        or row >= len(grid) 
        or col < 0 
        or col >= len(grid[0])
        or (row, col) in visited
        or grid[row][col] == 0):
            return 0
        visited.add((row, col))
        value = grid[row][col]
        # up
        value = max(value, grid[row][col] + self.path_value(grid, row-1, col, visited))
        # right
        value = max(value, grid[row][col] + self.path_value(grid, row, col+1, visited))
        # down
        value = max(value, grid[row][col] + self.path_value(grid, row+1, col, visited))
        # left
        value = max(value, grid[row][col] + self.path_value(grid, row, col-1, visited))

        visited.remove((row, col))

        return value

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold: int = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, self.path_value(grid, r, c, set()))

        return max_gold