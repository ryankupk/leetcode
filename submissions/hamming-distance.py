# https://leetcode.com/problems/hamming-distance

from itertools import zip_longest
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0

        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        print(f"{x_bin=}")
        print(f"{y_bin=}")
        if len(x_bin) > len(y_bin):
            y_bin = '0' * (len(x_bin) - len(y_bin)) + y_bin
        else:
            x_bin = '0' * (len(y_bin) - len(x_bin)) + x_bin

        print(f"{x_bin=}")
        print(f"{y_bin=}")
        
        for a, b in zip(x_bin, y_bin):
            if a != b:
                hamming_distance += 1
                
        return hamming_distance
        