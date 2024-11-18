/*
 * @lc app=leetcode id=3028 lang=golang
 *
 * [3028] Ant on the Boundary
 */

// @lc code=start
func returnToBoundaryCount(nums []int) int {
	res := 0
	currentPosition := 0

	for _, num := range nums {
		currentPosition += num
		if currentPosition == 0 {
			res++
		}
	}
    
	return res
}
// @lc code=end

