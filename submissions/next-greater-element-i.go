/*
 * @lc app=leetcode id=496 lang=golang
 *
 * [496] Next Greater Element I
 */

// @lc code=start
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	res := make([]int, len(nums1))
	nextGreatest := make(map[int]int)

outer:
	for i, val := range nums2 {
		for _, val2 := range nums2[i+1:] {
			if val2 > val {
				nextGreatest[val] = val2
				continue outer
			}
		}
		_, ok := nextGreatest[val]
		if !ok {
			nextGreatest[val] = -1
		}
	}

	for i, val := range nums1 {
		res[i] = nextGreatest[val]
	}

	return res
}

// @lc code=end

