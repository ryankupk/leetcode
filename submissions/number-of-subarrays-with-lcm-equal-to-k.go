/*
 * @lc app=leetcode id=2470 lang=golang
 *
 * [2470] Number of Subarrays With LCM Equal to K
 */

// @lc code=start
func subarrayLCM(nums []int, k int) int {
	count := 0
    
    for i := 0; i < len(nums); i++ {
        lcm := nums[i]
        for j := i; j < len(nums); j++ {
            lcm = lcm * nums[j] / gcd(lcm, nums[j])
            if lcm == k {
                count++
            }
            if lcm > k {
                break
            }
        }
    }
    
    return count
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}


// @lc code=end

