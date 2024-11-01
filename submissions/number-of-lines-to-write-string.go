/*
 * @lc app=leetcode id=806 lang=golang
 *
 * [806] Number of Lines To Write String
 */

// @lc code=start
func numberOfLines(widths []int, s string) []int {
	const lineLimit int = 100
	const indexOffset rune = 'a'

	lines := 1
	currentWidth := 0

	for _, val := range s {
		letterWidth := widths[val-indexOffset]
		if currentWidth+letterWidth <= lineLimit {
			currentWidth += letterWidth
		} else {
			lines += 1
			currentWidth = letterWidth
		}
	}
	return []int{lines, currentWidth}
}

// @lc code=end

