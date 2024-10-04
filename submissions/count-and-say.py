# https://leetcode.com/problems/count-and-say

class Solution:
    # n = 1: return 1 is the base case
    # n = 2: return count of last entry i.e. 1 1
    # n = 3: return count of last entry i.e. two 1's so 21
    # n=4: we have one 2 and one 1 so 1211   
    def countAndSay(self, n: int) -> str:
        dp = ["1"] * n
        def get_rle(chars):
            sets = []
            prev_char = None
            new_string = ""

            for char in chars:
                if char != prev_char:
                    prev_char = char
                    sets.append([])
                
                sets[-1].append(char)
            
            for set in sets:
                new_string += str(len(set))
                new_string += set[0]
            
            # prev_char = None
            # prev_char_count = 1
            # new_string = ""
            # for char in chars:
            #     if char == prev_char:
            #         prev_char_count += 1
            #         continue
            #     else:
            #         new_string += prev_char
            #         new_string += prev_char_count
            #         prev_char_count = 0
            #         prev_char = char
            # print(f"{sets=}")
            # print(f"{new_string=}")
            return new_string


        for i in range(1, n):
            dp[i] = get_rle(str(dp[i-1]))
                    
        # print(f"{dp=}")
        return dp[-1]

                
            
        