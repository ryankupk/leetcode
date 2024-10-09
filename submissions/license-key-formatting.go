/*
 * @lc app=leetcode id=482 lang=golang
 *
 * [482] License Key Formatting
 */

// @lc code=start
import (
	"strings"
)

func licenseKeyFormatting(s string, k int) string {
	newS := strings.ToUpper(strings.Join(strings.Split(s, "-"), ""))
	res := ""

	count := 0
	for i := len(newS) - 1; i >= 0; i-- {
		res = string(newS[i]) + res
		count++
		if count == k && i > 0 {
			res = "-" + res
			count = 0
		}
	}

	return res
}

// @lc code=end

