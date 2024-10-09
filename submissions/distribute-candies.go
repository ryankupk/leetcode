/*
 * @lc app=leetcode id=575 lang=golang
 *
 * [575] Distribute Candies
 */

// @lc code=start
func distributeCandies(candyType []int) int {
	limit := len(candyType) / 2
	set := make(map[int]bool)

	for _, val := range candyType {
		set[val] = true
	}

	return min(len(set), limit)
    
}
// @lc code=end

