/*
 * @lc app=leetcode id=451 lang=golang
 *
 * [451] Sort Characters By Frequency
 */

// @lc code=start
import (
	"slices"
)

func frequencySort(s string) string {
	counts := make(map[rune]int)
	list := make([]rune, len(s))

	for i, val := range s {
		counts[val]++
		list[i] = val
	}

	slices.SortFunc(list, func(i, j rune) int {
		if counts[i] < counts[j] {
			return 1
		} else if counts[i] > counts[j] {
			return -1
		} else if counts[i] == counts[j] {
			if i < j {
				return -1
			} else if j < i {
				return 1
			} else if i == j {
				return 0
			}
		}
		return 0
	})

	return string(list)
}

// @lc code=end
