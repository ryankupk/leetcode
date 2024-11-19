package main

/*
 * @lc app=leetcode id=2461 lang=golang
 *
 * [2461] Maximum Sum of Distinct Subarrays With Length K
 */

// @lc code=start

func maximumSubarraySum(nums []int, k int) int64 {
	var currentSum int64 = 0
	// counts := make(map[int]int)
	counts := [100001]int{}
	duplicateCount := 0
	for _, val := range nums[0:k] {
		counts[val]++
		if counts[val] == 2 {
			duplicateCount++
		}
		currentSum += int64(val)
	}
	var maxSum int64
	if duplicateCount > 0 {
		maxSum = 0
	} else {
		maxSum = currentSum
	}

	for i := 1; i < len(nums)-k+1; i++ {
		counts[nums[i-1]]--
		if counts[nums[i-1]] == 1 {
			duplicateCount--
		}
		counts[nums[i+k-1]]++
		if counts[nums[i+k-1]] == 2 {
			duplicateCount++
		}
		currentSum -= int64(nums[i-1])
		currentSum += int64(nums[i+k-1])
		if duplicateCount == 0 {
			maxSum = max(currentSum, maxSum)
		}
	}

	return maxSum
}

// @lc code=end
