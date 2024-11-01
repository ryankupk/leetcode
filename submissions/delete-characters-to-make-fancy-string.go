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

    res := []byte{s[0]}
    consecutive := 1

    for i := 1; i < len(s); i++ {
        if s[i] == s[i-1] {
            consecutive++
            if consecutive < 3 {
                res = append(res, s[i])
            }
        } else {
            consecutive = 1
            res = append(res, s[i])
        }
    }

    return string(res)
}

// @lc code=end

