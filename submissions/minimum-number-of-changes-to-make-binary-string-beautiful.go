/*
 * @lc app=leetcode id=2914 lang=golang
 *
 * [2914] Minimum Number of Changes to Make Binary String Beautiful
 */

// @lc code=start
func minChanges(s string) int {
	changes := 0

	for i := 0; i < len(s); i += 2 {
		if s[i:i+2] == "01" || s[i:i+2] == "10" {
			changes += 1
		}
	}

	return changes
}

// @lc code=end

