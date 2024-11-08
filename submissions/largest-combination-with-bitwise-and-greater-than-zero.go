/*
 * @lc app=leetcode id=2275 lang=golang
 *
 * [2275] Largest Combination With Bitwise AND Greater Than Zero
 */

// @lc code=start
import (
// "strconv"
)

func largestCombination(candidates []int) int {

	bitPositions := make([]int, 32)
	largest := -1

	for _, candidate := range candidates {
		i := 0
		for ; candidate > 0; candidate >>= 1 {
			bitVal := candidate & 1
			bitPositions[i] += bitVal
			largest = max(largest, bitPositions[i])
			i++
		}
	}
	return largest
}

// @lc code=end

