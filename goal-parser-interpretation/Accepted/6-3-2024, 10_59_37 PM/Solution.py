// https://leetcode.com/problems/goal-parser-interpretation

class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        for i in range(len(command)):
            if command[i] == 'G':
                result += 'G'
                continue
            if command[i] == '(' and command[i+1] == ')':
                result += 'o'
                i += 1
                continue
            if command[i] == '(' and command[i+1] == 'a':
                result += 'al'
                i += 2
                continue

        return result
        