# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        for sentence in sentences:
            most = max(len(sentence.split()), most)
            
        return most
        