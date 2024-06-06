// https://leetcode.com/problems/path-crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = [0,0]
        visited = set()
        visited.add((pos[0], pos[1]))
        for direction in path:
            if direction == "N":
                pos[0] += 1
            if direction == "E":
                pos[1] += 1
            if direction == "S":
                pos[0] -= 1
            if direction == "W":
                pos[1] -= 1
            if (pos[0], pos[1]) in visited:
                print(f"{pos=}")
                return True
            else:
                visited.add((pos[0], pos[1]))
            
        return False