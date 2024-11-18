/*
 * @lc app=leetcode id=1920 lang=golang
 *
 * [1920] Build Array from Permutation
 */

// @lc code=start
func buildArray(nums []int) []int {
	res := make([]int, len(nums))

	for i, val := range nums {
		res[i] = nums[val]
	}

	return res
}

// @lc code=end

