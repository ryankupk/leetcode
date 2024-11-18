/*
 * @lc app=leetcode id=682 lang=golang
 *
 * [682] Baseball Game
 */

// @lc code=start
func calPoints(operations []string) int {
	record := []int{}

	for _, operation := range operations {
		if operation == "+" {
			record = append(record, record[len(record)-1]+record[len(record)-2])
		} else if operation == "D" {
			record = append(record, 2*record[len(record)-1])
		} else if operation == "C" {
			record = record[:len(record)-1]
		} else {
			i, _ := strconv.Atoi(operation)
			record = append(record, i)
		}
	}

	sum := 0
	for _, val := range record {
		sum += val
	}

	return sum
}

// @lc code=end

