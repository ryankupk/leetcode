/*
 * @lc app=leetcode id=1574 lang=golang
 *
 * [1574] Shortest Subarray to be Removed to Make Array Sorted
 */

// @lc code=start
func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
    left, right := 0, n-1

    for left+1 < n && arr[left] <= arr[left+1] {
        left++
    }

    if left == n-1 {
        return 0
    }

    for right > left && arr[right-1] <= arr[right] {
        right--
    }

    result := min(n-left-1, right)

    i, j := 0, right
    for i <= left && j < n {
        if arr[i] <= arr[j] {
            result = min(result, j-i-1)
            i++
        } else {
            j++
        }
    }

    return result
}

// @lc code=end

