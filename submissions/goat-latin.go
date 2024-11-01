/*
 * @lc app=leetcode id=824 lang=golang
 *
 * [824] Goat Latin
 */

// @lc code=start
import (
	"strings"
)

func toGoatLatin(sentence string) string {
	split := strings.Split(sentence, " ")
	res := ""
	for i, val := range split {
		if val[0] == 'A' || val[0] == 'E' || val[0] == 'I' || val[0] == 'O' || val[0] == 'U' || val[0] == 'a' || val[0] == 'e' || val[0] == 'i' || val[0] == 'o' || val[0] == 'u' {
			res += val + "ma"
		} else {
			res += val[1:] + string(val[0]) + "ma"
		}
		for j := 0; j < i+1; j++ {
			res += "a"
		}
		res += " "
	}

	return res[:len(res)-1]
}

// @lc code=end

