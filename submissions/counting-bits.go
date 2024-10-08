/*
 * @lc app=leetcode id=338 lang=golang
 *
 * [338] Counting Bits
 */

// @lc code=start
func countBits(n int) []int {
	res := []int{}

	for i := 0; i <= n; i++ {
		bin := fmt.Sprintf("%032b", i)
		oneCount := 0
		for _, val := range bin {
			if val == '1' {
				oneCount += 1
			}
		}
		res = append(res, oneCount)
	}
	return res
}

// @lc code=end

