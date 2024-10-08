/*
 * @lc app=leetcode id=350 lang=golang
 *
 * [350] Intersection of Two Arrays II
 */

// @lc code=start
func intersect(nums1 []int, nums2 []int) []int {
	hash1 := make(map[int]int)
	hash2 := make(map[int]int)

	for _, val := range nums1 {
		hash1[val]++
	}
	for _, val := range nums2 {
		hash2[val]++
	}

	res := []int{}

	for val, _ := range hash1 {
		for i := 0; i < min(hash1[val], hash2[val]); i++ {
			res = append(res, val)
		}
	}

	return res
}

// @lc code=end

