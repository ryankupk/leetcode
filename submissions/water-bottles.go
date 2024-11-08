/*
 * @lc app=leetcode id=1518 lang=golang
 *
 * [1518] Water Bottles
 */

// @lc code=start
func numWaterBottles(numBottles int, numExchange int) int {
	emptyBottles := 0
	drank := 0

	for numBottles > 0 {
		drank += numBottles
		emptyBottles += numBottles
		numBottles = emptyBottles / numExchange
		emptyBottles = emptyBottles % numExchange
	}

	return drank
}
// @lc code=end

