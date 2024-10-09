/*
 * @lc app=leetcode id=605 lang=golang
 *
 * [605] Can Place Flowers
 */

// @lc code=start
func canPlaceFlowers(flowerbed []int, n int) bool {
	if n == 0 {
		return true
	}

	length := len(flowerbed)
	if length == 1 && flowerbed[0] == 0 {
		return true
	}

	if length > 1 && flowerbed[0] == 0 && flowerbed[1] == 0 {
		flowerbed[0] = 1
		n--
		if n == 0 {
			return true
		}
	}

	for i := 1; i < len(flowerbed)-1; i++ {
		if flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0 {
			flowerbed[i] = 1
			n--
		}
		if n == 0 {
			return true
		}
	}

	if length > 1 && flowerbed[length-1] == 0 && flowerbed[length-2] == 0 {
		flowerbed[length-1] = 1
		n--
	}

	if n == 0 {
		return true
	} else {
		return false
	}
}

// @lc code=end

