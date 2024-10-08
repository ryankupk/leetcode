/*
 * @lc app=leetcode id=190 lang=golang
 *
 * [190] Reverse Bits
 */

// @lc code=start
import (
	"fmt"
	"strconv"
)

func reverseBits(num uint32) uint32 {
	binaryString := fmt.Sprintf("%032b", num)
	reversedString := ""
	for i := len(binaryString) - 1; i >= 0; i-- {
		reversedString += string(binaryString[i])
	}
	reversedNum, err := strconv.ParseUint(reversedString, 2, 32)
	if err != nil {
		fmt.Println(err)
		return uint32(0)
	}

	return uint32(reversedNum)
}

// @lc code=end

