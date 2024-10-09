/*
 * @lc app=leetcode id=506 lang=golang
 *
 * [506] Relative Ranks
 */

// @lc code=start
import (
	"sort"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	res := make([]string, len(score))

	copied := make([]int, len(score))
	copy(copied, score)
	sort.Ints(copied)

	ranks := make(map[int]int)

	for i, val := range copied {
		ranks[val] = len(copied) - i
	}

	for i, val := range score {
		rank := ranks[val]
		if rank == 1 {
			res[i] = "Gold Medal"
		} else if rank == 2 {
			res[i] = "Silver Medal"
		} else if rank == 3 {
			res[i] = "Bronze Medal"
		} else {
			res[i] = strconv.Itoa(rank)
		}
	}

	return res
}

// @lc code=end

