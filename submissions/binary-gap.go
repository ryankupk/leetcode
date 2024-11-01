/*
 * @lc app=leetcode id=868 lang=golang
 *
 * [868] Binary Gap
 */

// @lc code=start
import (
	"fmt"
)

func binaryGap(n int) int {
	binaryString := fmt.Sprintf("%b", n)
    lastOneIndex := -1
    maxDistance := 0

    for i, char := range binaryString {
        if char == '1' {
            if lastOneIndex != -1 {
                maxDistance = max(maxDistance, i - lastOneIndex)
            }
            lastOneIndex = i
        }
    }

    return maxDistance
}


// @lc code=end

