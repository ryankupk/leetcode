# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def calculate_area(height_one, height_two, idx_one, idx_two):
            return abs(idx_one - idx_two) * min(height_one, height_two)

        p_one, p_two = 0, len(height)-1
        largest_area = 0

        while abs(p_one - p_two) > 0:
            # print(f"{p_one=}, {p_two=}, {largest_area=}")
            largest_area = max(
                largest_area, 
                calculate_area(height[p_one], height[p_two], p_one, p_two)
                )

            if height[p_one] > height[p_two]:
                p_two -= 1
            elif height[p_one] < height[p_two]:
                p_one += 1
            else:
                if p_one > p_two:
                    p_one += 1
                else:
                    p_two -= 1
            
        
        return largest_area
