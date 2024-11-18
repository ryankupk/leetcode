package main

/*
 * @lc app=leetcode id=67 lang=golang
 *
 * [67] Add Binary
 */

// @lc code=start
// I am not happy about any of this
import (
	"strings"
)

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func addBinary(a string, b string) string {
	if len(a) < len(b) {
		a = strings.Repeat("0", len(b)-len(a)) + a
	} else if len(b) < len(a) {
		b = strings.Repeat("0", len(a)-len(b)) + b
	}

	carry := 0
	var res strings.Builder
	for i := len(a) - 1; i >= 0; i-- {
		if a[i] == '0' && b[i] == '0' {
			if carry == 0 {
				res.WriteString("0")
			} else {
				res.WriteString("1")
				carry = 0
			}
		} else if a[i] == '0' && b[i] == '1' || a[i] == '1' && b[i] == '0' {
			if carry == 0 {
				res.WriteString("1")
			} else {
				res.WriteString("0")
				carry = 1
			}
		} else if a[i] == '1' && b[i] == '1' {
			if carry == 0 {
				res.WriteString("0")
				carry = 1
			} else {
				res.WriteString("1")
				carry = 1
			}
		}
	}
	if carry == 1 {
		res.WriteString("1")
	}
	return reverseString(res.String())
}

// @lc code=end
