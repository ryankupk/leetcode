/*
 * @lc app=leetcode id=2530 lang=golang
 *
 * [2530] Maximal Score After Applying K Operations
 */

// @lc code=start
import (
	"container/heap"
	"math"
)

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
	var score int64 = 0

	h := &IntHeap{}
	heap.Init(h)

	for _, val := range nums {
		heap.Push(h, val)
	}

	for i := 0; i < k; i++ {
		x := heap.Pop(h).(int)
		score += int64(x)
		newX := int(math.Ceil(float64(x) / 3))
		heap.Push(h, newX)
	}

	return score
}

// @lc code=end

