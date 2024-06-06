# https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        
        dp = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            row = [1]
            for j in range(len(dp[i-1])-1):
                row.append(dp[i-1][j] + dp[i-1][j+1])
            row.append(1)
            dp.append(row)

        return dp[-1]
        