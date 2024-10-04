// https://leetcode.com/problems/last-stone-weight

using System;
public class Solution {
    public int LastStoneWeight(int[] stones) {
        var maxHeap = new PriorityQueue<int, int>();

        foreach (int stone in stones) {
            maxHeap.Enqueue(stone, -stone);
        }

        while (maxHeap.Count > 1) {
            int stoneOne = maxHeap.Dequeue();
            int stoneTwo = maxHeap.Dequeue();
            int smashed = Math.Abs(stoneOne - stoneTwo);
            if (smashed > 0) {
                maxHeap.Enqueue(smashed, -smashed);
            }
        }

        var lastWeight = 0;
        if (maxHeap.Count > 0) {
            lastWeight = maxHeap.Dequeue();
        }

        return lastWeight;
        
    }
}