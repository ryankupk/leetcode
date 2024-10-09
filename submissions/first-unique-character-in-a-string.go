/*
 * @lc app=leetcode id=387 lang=golang
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
type IdxCount struct {
	idx   int
	count int
}

func firstUniqChar(s string) int {
	idx := 9999999999

	letterIdxCount := make(map[string]IdxCount)
	for i, val := range s {
		curIdxCount, ok := letterIdxCount[string(val)]
		if !ok {
			letterIdxCount[string(val)] = IdxCount{idx: i, count: 1}
			continue
		}
		newCount := curIdxCount.count + 1
		letterIdxCount[string(val)] = IdxCount{idx: curIdxCount.idx, count: newCount}
	}

	for _, curIdxCount := range letterIdxCount {
		if curIdxCount.count > 1 {
			continue
		}
		idx = min(curIdxCount.idx, idx)
	}

	if idx == 9999999999 {
		return -1
	}
	return idx
}

// @lc code=end

