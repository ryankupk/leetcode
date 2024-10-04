// https://leetcode.com/problems/add-strings

import (
	// "strconv"
	"fmt"
	"math/big"
)

func addStrings(num1 string, num2 string) string {
	num1Int := new(big.Int)
	num2Int := new(big.Int)

	_, ok1 := num1Int.SetString(num1, 10)
	_, ok2 := num2Int.SetString(num2, 10)

	if !ok1 || !ok2 {
		return "oops"
	}

	result := new(big.Int)
	result.Add(num1Int, num2Int)

	return result.String()
}
