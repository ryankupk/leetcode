func oddCells(m int, n int, indices [][]int) int {
    mat := make([][]int, m) 
    for i := 0; i < m; i++ {
        mat[i] = make([]int, n)
    }
    odds := 0
    for _, query := range indices {
        row, col := query[0], query[1]

        for i := range mat[row] {
            mat[row][i]++
            if mat[row][i] % 2 == 0 {
                odds--
            } else {
                odds++
            }
        }

        for i := range len(mat) {
            mat[i][col]++
            if mat[i][col] % 2 == 0 {
                odds--
            } else {
                odds++
            }
        }
    }

    return odds
}
