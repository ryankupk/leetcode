// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for charact in s:
            if charact == '(':
                stack.append(charact)
            if charact == ')':
                try:
                    popped = stack.pop()
                    if popped != '(':
                        return False
                except:
                    return False
            if charact == '[':
                stack.append(charact)
            if charact == ']':
                try:
                    popped = stack.pop()
                    if popped != '[':
                        return False
                except:
                    return False
            if charact == '{':
                stack.append(charact)
            if charact == '}':
                try:
                    popped = stack.pop()
                    if popped != '{':
                        return False
                except:
                    return False
        if len(stack) != 0:
            return False

        return True