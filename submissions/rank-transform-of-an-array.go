// https://leetcode.com/problems/rank-transform-of-an-array

import (
	"sort"
)

func arrayRankTransform(arr []int) []int {

	ranks := make(map[int]int)
	sorted := make([]int, len(arr))
	copy(sorted, arr)

	sort.Ints(sorted)

	curRank := 0

	for _, val := range sorted {
		_, ok := ranks[val]
		if !ok {
			curRank++
			ranks[val] = curRank
		}
	}

	ranked := make([]int, len(arr))

	for i, val := range arr {
		ranked[i] = ranks[val]
	}

	return ranked
}
