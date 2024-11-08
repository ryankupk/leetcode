/*
 * @lc app=leetcode id=1829 lang=golang
 *
 * [1829] Maximum XOR for Each Query
 */

// @lc code=start
import (
	"math"
)

func getMaximumXor(nums []int, maximumBit int) []int {
	kLimit := int(math.Pow(2, float64(maximumBit))) - 1

	res := make([]int, len(nums))

	xord := 0
	for _, val := range nums {
		xord ^= val
	}

	for i := len(nums) - 1; i >= 0; i-- {
		optimalK := xord ^ kLimit
		res[len(nums)-i-1] = optimalK
		if i > 0 {
            xord ^= nums[i]
        }
	}

	return res
}

// @lc code=end

