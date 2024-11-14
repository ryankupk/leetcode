/*
 * @lc app=leetcode id=260 lang=golang
 *
 * [260] Single Number III
 */

// @lc code=start
func singleNumber(nums []int) []int {
	res := make([]int, 2)
	counts := make(map[int]int)

	for _, num := range nums {
		counts[num]++
	}

	firstAdded := false
	for k, v := range counts {
		if v == 1 {
			if firstAdded {
				res[1] = k
			} else {
				res[0] = k
				firstAdded = true
			}
		}
	}
	return res
}

// @lc code=end

