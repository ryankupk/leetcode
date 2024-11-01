/*
 * @lc app=leetcode id=73 lang=golang
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
func setZeroes(matrix [][]int) {
	rows, cols := make(map[int]bool), make(map[int]bool)

	for i, row := range matrix {
		for j, val := range row {
			if val == 0 {
				rows[i] = true
				cols[j] = true
			}
		}
	}

	for row, _ := range rows {
		for i := 0; i < len(matrix[0]); i++ {
			matrix[row][i] = 0
		}
	}

	for col, _ := range cols {
		for _, row := range matrix {
			row[col] = 0
		}
	}
}

// @lc code=end

