// https://leetcode.com/problems/max-consecutive-ones

import "slices"
func findMaxConsecutiveOnes(nums []int) int {
	maxConsecutive := []int{}
	currentConsecutive := 0

	for _, num := range nums {
		if num == 0 {
			maxConsecutive = append(maxConsecutive, currentConsecutive)
			currentConsecutive = 0
		} else {
			currentConsecutive += 1
		}

	}
	if nums[len(nums)-1] != 0 {
		maxConsecutive = append(maxConsecutive, currentConsecutive)
	}
	fmt.Println(maxConsecutive)

	return slices.Max(maxConsecutive)
	// return 0

}
