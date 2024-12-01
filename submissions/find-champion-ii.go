package main

/*
 * @lc app=leetcode id=2924 lang=golang
 *
 * [2924] Find Champion II
 */

// @lc code=start
import (
	"sort"
)

func findChampion(n int, edges [][]int) int {
	ranks := make([][]int, n)

	for i := 0; i < n; i++ {
		ranks[i] = []int{i, 0}
	}

	for _, edge := range edges {
		ranks[edge[1]][1]++
	}

	sort.Slice(ranks, func(i, j int) bool {
		return ranks[i][1] < ranks[j][1]
	})

	if len(ranks) > 1 && ranks[0][1] == ranks[1][1] {
		return -1
	}

	return ranks[0][0]
}

// @lc code=end
