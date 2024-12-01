package main
/*
 * @lc app=leetcode id=841 lang=golang
 *
 * [841] Keys and Rooms
 */

// @lc code=start
func canVisitAllRooms(rooms [][]int) bool {
	adj := []int{}
	visited := make(map[int]bool)
	for _, key := range rooms[0] {
		adj = append(adj, key)
	}
	visited[0] = true

	for len(adj) > 0 {
		next := adj[len(adj)-1]
		adj = adj[:len(adj)-1]
		haveVisited, ok := visited[next]
		if !ok || !haveVisited {
			visited[next] = true
			adj = append(adj, rooms[next]...)
		}
	}

	for i := 1; i < len(rooms); i++ {
		_, ok := visited[i] // `ok` being false OR the first return value being false would indicate that the room has not been visited
		if !ok {
			return false
		}
	}

	return true
}

// @lc code=end

