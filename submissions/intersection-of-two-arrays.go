/*
 * @lc app=leetcode id=349 lang=golang
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
func intersection(nums1 []int, nums2 []int) []int {
	hash1 := make(map[int]bool)

	for _, val := range nums1 {
		hash1[val] = true
	}

	res := []int{}

	for _, val := range nums2 {
		in := hash1[val]
		if in {
			res = append(res, val)
			hash1[val] = false
		}
	}

	return res
}
// @lc code=end

