// https://leetcode.com/problems/missing-number

func missingNumber(nums []int) int {
	var sumtorial int
	var limit int = len(nums)
	for i := 0; i < limit+1; i++ {
		sumtorial += i
	}

	for i := 0; i < limit; i++ {
		sumtorial -= nums[i]
	}

	return sumtorial
    
}