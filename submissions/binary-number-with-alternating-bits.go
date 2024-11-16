/*
 * @lc app=leetcode id=693 lang=golang
 *
 * [693] Binary Number with Alternating Bits
 */

// @lc code=start
func hasAlternatingBits(n int) bool {
	prevBit := n & 1
	n >>= 1

	for n > 0 {
		bit := n & 1
		if bit == prevBit {
			return false
		}
		prevBit = bit
		n >>= 1
	}

	return true
}

// @lc code=end

