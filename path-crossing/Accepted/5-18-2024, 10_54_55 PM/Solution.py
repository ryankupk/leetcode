# https://leetcode.com/problems/path-crossing

from copy import copy
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [0,0]
        visited = []
        visited.append(copy(pos))
        for direction in path:
            if direction == "N":
                pos[0] += 1
            if direction == "E":
                pos[1] += 1
            if direction == "S":
                pos[0] -= 1
            if direction == "W":
                pos[1] -= 1
            if pos in visited:
                print(f"{pos=}")
                return True
            else:
                visited.append(copy(pos))
            
        return False