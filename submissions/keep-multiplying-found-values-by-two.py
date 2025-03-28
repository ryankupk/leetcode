class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = {num for num in nums if num >= original and num % original == 0}
        while True:
            if original in nums_set:
                original *= 2
            else:
                return original
