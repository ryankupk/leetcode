/*
 * @lc app=leetcode id=917 lang=golang
 *
 * [917] Reverse Only Letters
 */

// @lc code=start
func reverseOnlyLetters(s string) string {
    runes := []rune(s)
    left, right := 0, len(runes)-1

    for left < right {
        for left < right && !isLetter(runes[left]) {
            left++
        }
        for left < right && !isLetter(runes[right]) {
            right--
        }
        if left < right {
            runes[left], runes[right] = runes[right], runes[left]
            left++
            right--
        }
    }

    return string(runes)
}

func isLetter(r rune) bool {
    return (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z')
}

// @lc code=end

