# https://leetcode.com/problems/roman-to-integer

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
        sum_nums = 0
        flag = False
        for idx, char in enumerate(s):
            if flag:
                flag = False
                continue
            if idx+1 < len(s) and char in combinations.keys() and s[idx+1] in combinations[char]:
                if char == list(combinations.keys())[0]:
                    sum_nums += values[s[idx+1]]-1
                    # nums.append(
                elif char == list(combinations.keys())[1]:
                    sum_nums += values[s[idx+1]]-10
                    # nums.append(values[s[idx+1]]-10)
                elif char == list(combinations.keys())[2]:
                    sum_nums += values[s[idx+1]]-100
                    # nums.append(values[s[idx+1]]-100)
                flag = True
            else:
                sum_nums += values[s[idx]]
                # nums.append(values[char])
            
        return sum_nums