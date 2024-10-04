# https://leetcode.com/problems/count-items-matching-a-rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        rule_index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        count = 0
        for item in items:
            if item[rule_index[ruleKey]] == ruleValue:
                count += 1
                
        return count
    