/*
 * @lc app=leetcode id=3163 lang=golang
 *
 * [3163] String Compression III
 */

// @lc code=start
import (
// "strconv"
)

func compressedString(word string) string {
	maxPrefix := 9
	word += "9" // arbitrary buffer to move past the end of the string
	comp := []byte{}
	currentPrefixLength := 0
	currentPrefixLetter := word[0]

	for i := 1; i < len(word); i++ {
		if (currentPrefixLength == maxPrefix-1 && word[i] == currentPrefixLetter) || word[i] != currentPrefixLetter {
			comp = append(comp, byte('1'+currentPrefixLength), currentPrefixLetter)
			currentPrefixLength = 0
			currentPrefixLetter = word[i]
		} else {
			currentPrefixLength++
		}
	}

	return string(comp)
}

// @lc code=end

