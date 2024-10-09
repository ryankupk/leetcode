/*
 * @lc app=leetcode id=921 lang=golang
 *
 * [921] Minimum Add to Make Parentheses Valid
 */

// @lc code=start
func minAddToMakeValid(s string) int {
	open, close := 0, 0

	for _, val := range s {
		if val == '(' {
			open++
		}
		if val == ')' {
			if open > 0 {
				open--
			} else {
				close++
			}
		}
	}
	return open + close
}

// @lc code=end

