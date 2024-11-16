/*
 * @lc app=leetcode id=412 lang=golang
 *
 * [412] Fizz Buzz
 */

// @lc code=start
import (
	"strconv"
)

func fizzBuzz(n int) []string {
	res := make([]string, n+1)

	for i := 1; i <= n; i++ {
		if i%3 == 0 {
			res[i] += "Fizz"
		}
		if i%5 == 0 {
			res[i] += "Buzz"
		}
		if i%3 != 0 && i%5 != 0 {
			res[i] += strconv.Itoa(i)
		}
	}

	return res[1:]
}

// @lc code=end

