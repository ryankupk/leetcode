# https://leetcode.com/problems/largest-number


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Convert numbers to strings
        nums_str = list(map(str, nums))
        
        # Custom comparator to sort numbers in the desired order
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        nums_str.sort(key=functools.cmp_to_key(compare))
        
        # Join the sorted strings
        largest_num = ''.join(nums_str)
        
        # Handle the case where the largest number is '0'
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num

        return largest_num        