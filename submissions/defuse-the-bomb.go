/*
 * @lc app=leetcode id=1652 lang=golang
 *
 * [1652] Defuse the Bomb
 */

// @lc code=start
func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
func decrypt(code []int, k int) []int {

	res := make([]int, len(code))
	if k == 0 {
		return res
	}

	for i := range code {
		if k < 0 {
			for j := 1; j <= abs(k); j++ {
				idx := i - j
				if idx < 0 {
					idx += len(code)
				}
				res[i] += code[idx]
			}
		} else if k > 0 {
			for j := 1; j <= abs(k); j++ {
				idx := i + j
				if idx >= len(code) {
					idx -= len(code)
				}
				res[i] += code[idx]
			}
		}
	}

	return res
}

// @lc code=end

