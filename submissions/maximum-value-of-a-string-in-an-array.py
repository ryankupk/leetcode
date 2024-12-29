class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        values = [0] * len(strs)
        for i, string in enumerate(strs):
            if all((char.isdigit() for char in string)):
                values[i] = int(string)
            else:
                values[i] = len(string)
        
        return max(values)
