// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        combinations = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }
        nums = []
        flag = False
        for idx, char in enumerate(s):
            if flag:
                flag = False
                continue
            if idx+1 < len(s) and char in combinations.keys() and s[idx+1] in combinations[char]:
                if char == list(combinations.keys())[0]:
                    nums.append(values[s[idx+1]]-1)
                elif char == list(combinations.keys())[1]:
                    nums.append(values[s[idx+1]]-10)
                elif char == list(combinations.keys())[2]:
                    nums.append(values[s[idx+1]]-100)
                flag = True
            else:
                nums.append(values[char])
            
        return sum(nums)