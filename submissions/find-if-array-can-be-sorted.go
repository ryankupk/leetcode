/*
 * @lc app=leetcode id=3011 lang=golang
 *
 * [3011] Find if Array Can Be Sorted
 */

// @lc code=start
import (
	"strconv"
	"slices"
)

func canSortArray(nums []int) bool {
	if len(nums) <= 1 {
		return true
	}

	bitCounts := make([]int, len(nums))

	for i, val := range nums {
		bitString := fmt.Sprintf("%b", val)
		bitCount := 0
		for _, val := range bitString {
			intVal, _ := strconv.Atoi(string(val))
			bitCount += intVal
		}
		bitCounts[i] = bitCount
	}

	likeBitsIdxRanges := [][]int{}

	currentCount := bitCounts[0]
	startingIdx := 0
	for i := 1; i < len(bitCounts); i++ {
		if bitCounts[i] != currentCount {
			likeBitsIdxRanges = append(likeBitsIdxRanges, []int{startingIdx, i})
			startingIdx = i
			currentCount = bitCounts[i]
		}
	}
	if len(likeBitsIdxRanges) == 0 {
		return true
	}
	likeBitsIdxRanges = append(likeBitsIdxRanges, []int{likeBitsIdxRanges[len(likeBitsIdxRanges)-1][1], len(bitCounts)})

	for i := 0; i < len(likeBitsIdxRanges)-1; i++ {
		lowerSet := nums[likeBitsIdxRanges[i][0]:likeBitsIdxRanges[i][1]]
		upperSet := nums[likeBitsIdxRanges[i+1][0]:likeBitsIdxRanges[i+1][1]]
		if slices.Max(lowerSet) > slices.Min(upperSet) {
			return false
		}
	}

	return true
}

// @lc code=end

