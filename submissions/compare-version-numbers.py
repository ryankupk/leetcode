class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split, v2_split = list(map(int,version1.split('.'))), list(map(int, version2.split('.')))
        if len(v1_split) < len(v2_split):
            v1_split.extend([0 for i in range(len(v2_split) - len(v1_split))])
        elif len(v1_split) > len(v2_split):
            v2_split.extend([0 for i in range(len(v1_split) - len(v2_split))])

        for a, b in zip(v1_split, v2_split):
            if a < b:
                return -1
            if a > b:
                return 1
        
        return 0
