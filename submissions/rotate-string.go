/*
 * @lc app=leetcode id=796 lang=golang
 *
 * [796] Rotate String
 */

// @lc code=start
func rotateString(s string, goal string) bool {
	for i := 0; i < len(s); i++ {
		s = string(s[1:]) + string(s[0])
		if s == goal {
			return true
		}
	}
	return false
}

// @lc code=end

