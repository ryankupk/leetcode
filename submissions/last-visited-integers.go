/*
 * @lc app=leetcode id=2899 lang=golang
 *
 * [2899] Last Visited Integers
 */

// @lc code=start
func lastVisitedIntegers(nums []int) []int {
	seen := []int{}
	ans := []int{}

	k := 0
	for _, num := range nums {
		if num >= 0 {
			seen = append([]int{num}, seen...)
			k = 0
		} else {
			k++
			if k <= len(seen) {
				ans = append(ans, seen[k-1])
			} else {
				ans = append(ans, -1)
			}
		}
	}
	return ans
}

// @lc code=end

