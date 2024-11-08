/*
 * @lc app=leetcode id=2299 lang=golang
 *
 * [2299] Strong Password Checker II
 */

// @lc code=start
import (
	"strings"
)

func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}

	validCharacters := "!@#$%^&*()-+"

	oneUppercase := false
	oneLowercase := false
	oneDigit := false
	oneSpecial := false
	prevChar := password[0]

	if prevChar >= 'A' && prevChar <= 'Z' {
		oneUppercase = true
	} else if prevChar >= 'a' && prevChar <= 'z' {
		oneLowercase = true
	} else if prevChar >= '0' && prevChar <= '9' {
		oneDigit = true
	} else if strings.ContainsAny(string(prevChar), validCharacters) {
		oneSpecial = true
	}

	for i := 1; i < len(password); i++ {
		if password[i] == prevChar {
			return false
		} else if password[i] >= 'A' && password[i] <= 'Z' {
			oneUppercase = true
		} else if password[i] >= 'a' && password[i] <= 'z' {
			oneLowercase = true
		} else if password[i] >= '0' && password[i] <= '9' {
			oneDigit = true
		} else if strings.ContainsAny(string(password[i]), validCharacters) {
			oneSpecial = true
		}
		prevChar = password[i]
	}
	return oneUppercase && oneLowercase && oneDigit && oneSpecial
}

// @lc code=end

