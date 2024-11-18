/*
 * @lc app=leetcode id=151 lang=golang
 *
 * [151] Reverse Words in a String
 */

// @lc code=start
import (
	"strings"
)
func reverseWords(s string) string {
    var res strings.Builder

	split := strings.Fields(s)

	for i := len(split)-1; i > 0; i-- {
		res.WriteString(split[i])
		res.WriteString(" ")
	}
	res.WriteString(split[0])

	return res.String()
}
// @lc code=end

