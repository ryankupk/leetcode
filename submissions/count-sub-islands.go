// https://leetcode.com/problems/count-sub-islands

type coordinate struct {
	x int
	y int
}

func dfs(x, y, rows, cols int, visited *map[coordinate]bool, grid1 [][]int, grid2 [][]int) bool {
    coord := coordinate{x, y}
    
    if x < 0 || y < 0 || x >= rows || y >= cols || grid2[x][y] == 0 || (*visited)[coord] {
        return true
    }

    (*visited)[coord] = true

	res := grid1[x][y] == 1
	if grid1[x][y] == 0 {
		res = false
	}

	res = dfs(x+1, y, rows, cols, visited, grid1, grid2) && res
	res = dfs(x-1, y, rows, cols, visited, grid1, grid2) && res
	res = dfs(x, y+1, rows, cols, visited, grid1, grid2) && res
	res = dfs(x, y-1, rows, cols, visited, grid1, grid2) && res
	return res
}

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	var rows, cols = len(grid1), len(grid1[0])
	var visited = make(map[coordinate]bool)

	count := 0
	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			if grid2[x][y] == 1 && !visited[coordinate{x, y}] == true && dfs(x, y, rows, cols, &visited, grid1, grid2) == true {
				count += 1
			}
		}
	}
	return count

}
