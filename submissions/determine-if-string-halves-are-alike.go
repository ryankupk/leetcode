package main

/*
 * @lc app=leetcode id=1704 lang=golang
 *
 * [1704] Determine if String Halves Are Alike
 */

// @lc code=start
import (
	"strings"
)

func halvesAreAlike(s string) bool {
	vowels := "aeiouAIEOU"

	left, right := s[:len(s)/2], s[len(s)/2:]

	leftCount, rightCount := 0, 0

	for i := 0; i < len(left); i++ {
		if strings.ContainsRune(vowels, rune(left[i])) {
			leftCount++
		}
		if strings.ContainsRune(vowels, rune(right[i])) {
			rightCount++
		}
	}

	return leftCount == rightCount

}

// @lc code=end
