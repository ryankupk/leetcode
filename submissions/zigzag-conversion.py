# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ['' for _ in range(numRows)]
        cur_row = 0
        direction = 1
        for letter in s:
            rows[cur_row] += (letter)
            if cur_row == numRows - 1 and direction == 1:
                direction = -1
            if cur_row == 0 and direction == -1:
                direction = 1

            cur_row += direction

        final_string = ''.join((substring for substring in rows))
        return final_string
            
        
        
        