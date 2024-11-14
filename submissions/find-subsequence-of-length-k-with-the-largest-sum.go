/*
 * @lc app=leetcode id=2099 lang=golang
 *
 * [2099] Find Subsequence of Length K With the Largest Sum
 */

// @lc code=start
import (
	"sort"
)

func maxSubsequence(nums []int, k int) []int {
	pairs := make([][2]int, len(nums))
	for i, val := range nums {
		pairs[i] = [2]int{i, val}
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] > pairs[j][1]
	})

	selected := pairs[:k]

	sort.Slice(selected, func(i, j int) bool {
		return pairs[i][0] < pairs[j][0]
	})

	res := make([]int, len(selected))

	for i, pair := range selected {
		res[i] = pair[1]
	}

	return res
}

// @lc code=end

