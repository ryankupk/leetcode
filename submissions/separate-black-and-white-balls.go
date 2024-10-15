/*
 * @lc app=leetcode id=2938 lang=golang
 *
 * [2938] Separate Black and White Balls
 */

// @lc code=start
func minimumSteps(s string) int64 {
	var (
		oneCount int64 = 0
		total    int64 = 0
	)

	for _, val := range s {
		if val == '1' {
			oneCount++
		} else {
			total += oneCount
		}
	}

	return total
}

// @lc code=end

