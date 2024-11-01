/*
 * @lc app=leetcode id=844 lang=golang
 *
 * [844] Backspace String Compare
 */

// @lc code=start
func buildStack(stack []rune, word string) []rune {
	for _, letter := range word {
		if letter != '#' {
			stack = append(stack, letter)
		} else if len(stack) > 0 && letter == '#' {
			stack = stack[:len(stack)-1]
		}
	}

	return stack
}

func backspaceCompare(s string, t string) bool {
	stackOne, stackTwo := []rune{}, []rune{}

	stackOne = buildStack(stackOne, s)
	stackTwo = buildStack(stackTwo, t)

	if len(stackOne) != len(stackTwo) {
		return false
	}

	for i, _ := range stackOne {
		if stackOne[i] != stackTwo[i] {
			return false
		}
	}

	return true
}

// @lc code=end

