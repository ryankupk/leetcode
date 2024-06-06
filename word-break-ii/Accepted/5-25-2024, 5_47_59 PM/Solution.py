# https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start, path):
            if start == len(s):
                res.append(' '.join(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and dp[end]:
                    dfs(end, path + [s[start:end]])
        
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        res = []
        if dp[-1]:
            dfs(0, [])
        
        return res