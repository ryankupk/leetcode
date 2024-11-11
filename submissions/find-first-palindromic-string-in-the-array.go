/*
 * @lc app=leetcode id=2108 lang=golang
 *
 * [2108] Find First Palindromic String in the Array
 */

// @lc code=start
func isPalindrome(word string) bool {
	i, j := 0, len(word)-1
	for i < j {
		if word[i] != word[j] {
			return false
		}
		i++
		j--
	}
	return true
}
func firstPalindrome(words []string) string {
	for _, word := range words {
		if isPalindrome(word) {
			return word
		}
	}

	return ""
}

// @lc code=end

