# https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(letters)
        for letter in letters:
            if letter > target:
                return letter

        return letters[0]
        