/*
 * @lc app=leetcode id=2610 lang=golang
 *
 * [2610] Convert an Array Into a 2D Array With Conditions
 */

// @lc code=start
func findMatrix(nums []int) [][]int {
	highestCount := 0

	counts := make(map[int]int)
	for _, val := range nums {
		counts[val]++
		highestCount = max(highestCount, counts[val])
	}

	res := make([][]int, highestCount)

	for i := 0; i < highestCount; i++ {
		for k, v := range counts {
			if v > 0 {
				res[i] = append(res[i], k)
				counts[k]--
			} else {
				delete(counts, k)
			}
		}
	}

	return res
}

// @lc code=end

