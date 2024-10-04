// https://leetcode.com/problems/number-of-islands

import (
	"fmt"
)

type coordinate struct {
	x int
	y int
}

func bfs(x, y, maxX, maxY int, grid [][]byte, visited *map[coordinate]bool) bool {
	queue := []coordinate{}
	(*visited)[coordinate{x, y}] = true
	queue = append(queue, coordinate{x, y})

	for len(queue) > 0 {
		curCoord := queue[0]
		queue = queue[1:]

		directions := [][]int{
			{0, 1},
			{1, 0},
			{0, -1},
			{-1, 0},
		}
		for _, direction := range directions {
			curDirection := coordinate{curCoord.x + direction[0], curCoord.y + direction[1]}
			if curDirection.x >= 0 && curDirection.x < maxX && curDirection.y >= 0 && curDirection.y < maxY && grid[curDirection.x][curDirection.y] == 49 && (*visited)[curDirection] == false {
				queue = append(queue, coordinate{curDirection.x, curDirection.y})
				(*visited)[coordinate{curDirection.x, curDirection.y}] = true
			}
		}
	}
	return false
}

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	var rows, cols = len(grid), len(grid[0])

	visited := make(map[coordinate]bool)
	islandCount := 0

	for x, row := range grid {
		for y, _ := range row {
			if grid[x][y] == 49 && visited[coordinate{x, y}] == false {
				bfs(x, y, rows, cols, grid, &visited)
				islandCount += 1
			}
		}
	}

	return islandCount

}
