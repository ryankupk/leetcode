/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
import (
	"strconv"
)

func isPalindrome(x int) bool {
	strung := strconv.Itoa(x)
	left, right := 0, len(strung)-1
	for left < right {
		if strung[left] != strung[right] {
			return false
		}
		left++
		right--
	}
	return true
}

// @lc code=end

