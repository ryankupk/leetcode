/*
 * @lc app=leetcode id=2696 lang=golang
 *
 * [2696] Minimum String Length After Removing Substrings
 */

// @lc code=start
func minLength(s string) int {
	r1, r2 := "AB", "CD"

	for i := 0; i < len(s)-1; i++ {
		if s[i:i+2] == r1 || s[i:i+2] == r2 {
			s = s[:i] + s[i+2:]
			i = -1
			continue
		}

	}
	return len(s)
}

// @lc code=end

