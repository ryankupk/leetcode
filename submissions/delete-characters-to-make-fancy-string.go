/*
 * @lc app=leetcode id=1957 lang=golang
 *
 * [1957] Delete Characters to Make Fancy String
 */

// @lc code=start
func makeFancyString(s string) string {
	if len(s) < 3 {
		return s
	}

	// res := []byte{s[0]}
	res := make([]byte, len(s))
	res[0] = s[0]
	resIdx := 1
	addedChars := 1
	consecutive := 1

	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			consecutive++
			if consecutive < 3 {
				// res = append(res, s[i])
				res[resIdx] = s[i]
				resIdx++
				addedChars++
			}
		} else {
			consecutive = 1
			// res = append(res, s[i])
			res[resIdx] = s[i]
			resIdx++
			addedChars++
		}
	}

	return string(res[:addedChars])
}

// @lc code=end

