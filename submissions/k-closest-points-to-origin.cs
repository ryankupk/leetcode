// https://leetcode.com/problems/k-closest-points-to-origin

using System;
public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        var minHeap = new PriorityQueue<int[], int>();
        foreach (int[] point in points) {
            var distance = (point[0] * point[0]) + (point[1] * point[1]);
            minHeap.Enqueue(point, Math.Abs(distance));
        }

        int[][] returnArr = new int[k][];
        for (int i = 0; i < k; ++i) {
            var item = minHeap.Dequeue();
            returnArr[i] = item;
        }

        return returnArr;
        
    }
}