// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        
        dp = [[1], [1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(len(dp[i-1])-1):
                row.append(dp[i-1][j] + dp[i-1][j+1])
            row.append(1)
            dp.append(row)

        return dp