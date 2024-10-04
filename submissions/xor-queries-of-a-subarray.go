// https://leetcode.com/problems/xor-queries-of-a-subarray

func xorQueries(arr []int, queries [][]int) []int {
	ret := make([]int, len(queries))
	for i, query := range queries {
		xord := 0
		for _, num := range arr[query[0] : query[1]+1] {
			xord ^= num
		}
		ret[i] = xord
	}

	return ret
}
