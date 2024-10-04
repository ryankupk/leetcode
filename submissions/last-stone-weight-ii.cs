// https://leetcode.com/problems/last-stone-weight-ii

using System.Collections.Generic;
public class Solution {
    public int DFS(int i, int total, int target, int len, int stoneSum, int[] stones, Dictionary<Tuple<int, int>, int> dp) {
        if (total >= target || i == len) {
            return Math.Abs(total - (stoneSum - total));
        }
        if (dp.ContainsKey(new Tuple<int, int>(i, total))) {
            return dp[new Tuple<int, int>(i, total)];
        }

        dp[new Tuple<int, int>(i, total)] = Math.Min(DFS(i+1, total, target, len, stoneSum, stones, dp), DFS(i+1, total+stones[i], target, len, stoneSum, stones, dp));

        return dp[new Tuple<int, int>(i, total)];
    }
    public int LastStoneWeightII(int[] stones) {
        var dp = new Dictionary<Tuple<int, int>, int>();
        int mid = 0;
        int stoneSum = 0;
        foreach (int stone in stones) {
            stoneSum += stone;
        }
        mid = (int)Math.Ceiling((double)stoneSum / 2); // midpoint is ceiling of sum / 2

        return DFS(0, 0, mid, stones.Length, stoneSum, stones, dp);

    }
}