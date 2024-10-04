// https://leetcode.com/problems/third-maximum-number

import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func thirdMax(nums []int) int {
	h := &IntHeap{}
    heap.Init(h)
    seen := make(map[int]bool)

    for _, num := range nums {
        if !seen[num] {
            if h.Len() < 3 {
                heap.Push(h, num)
            } else if num > (*h)[0] {
                heap.Pop(h)
                heap.Push(h, num)
            }
            seen[num] = true
        }
    }

    if h.Len() < 3 {
        // If there are fewer than 3 distinct numbers, return the maximum
        for h.Len() > 1 {
            heap.Pop(h)
        }
        return (*h)[0]
    }

    return (*h)[0] // The smallest of the three largest numbers

}
