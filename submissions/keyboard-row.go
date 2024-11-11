/*
 * @lc app=leetcode id=500 lang=golang
 *
 * [500] Keyboard Row
 */

// @lc code=start
import (
	"strings"
)

func findWords(words []string) []string {
	rows := []string{"qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKJL", "zxcvbnmZXCVBNM"}
	res := []string{}

outer:
	for _, word := range words {

		neededRow := -1

		for i, row := range rows {
			if strings.ContainsAny(row, string(word[0])) {
				neededRow = i
				break
			}
		}

		for _, letter := range word[1:] {
			if !strings.ContainsAny(rows[neededRow], string(letter)) {
				continue outer
			}
		}
		res = append(res, word)
	}

	return res
}

// @lc code=end

