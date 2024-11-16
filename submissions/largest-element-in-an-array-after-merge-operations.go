/*
 * @lc app=leetcode id=2789 lang=golang
 *
 * [2789] Largest Element in an Array after Merge Operations
 */

// @lc code=start
import (
	"slices"
)

func maxArrayValue(nums []int) int64 {
	n := len(nums)
	if n == 1 {
		return int64(nums[0])
	} else if n == 2 {
		if nums[1] >= nums[0] {
			return int64(nums[0] + nums[1])
		} else {
			return int64(nums[0])
		}
	}

	for i := n - 2; i >= 0; i-- {
		if nums[i+1] >= nums[i] {
			nums[i+1] += nums[i]
			nums = append(nums[:i], nums[i+1:]...)
		}
	}

	return int64(slices.Max(nums))
}

// @lc code=end

