# https://leetcode.com/problems/valid-sudoku

from collections import Counter, defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counted = Counter((i for i in row if i != '.'))
            if len([i for i in counted.values() if i > 1]) > 0:
                return False
        for i in range(len(board)):
            column = [row[i] for row in board if row[i] != '.']
            counted = Counter(column)
            if len([val for val in counted.values() if val > 1]) > 0:
                return False

        for h in range(0, 9, 3):    
            for k in range(0, 9, 3):
                cell_counter = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        # print(f"{board[h + i][k + j]=}")
                        # print(f"{cell_counter=}")
                        # print(f"{}")
                        if board[h + i][k + j] != ".":
                            cell_counter[board[h + i][k + j]] += 1
                if len([val for val in cell_counter.values() if val > 1]) > 0:
                    return False
            
                
        return True