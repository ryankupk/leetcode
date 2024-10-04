// https://leetcode.com/problems/course-schedule

import (
// "fmt"
)

func dfs(parent int, adjacencies map[int][]int, visited *map[int]bool) bool {
	if (*visited)[parent] == true {
		return false
	}
	if len(adjacencies[parent]) == 0 {
		return true
	}

	(*visited)[parent] = true

	for _, child := range adjacencies[parent] {
		childCompletable := dfs(child, adjacencies, visited)
		if childCompletable == false {
			return false
		}

	}
	(*visited)[parent] = false
	adjacencies[parent] = []int{}
	return true
}

func canFinish(numCourses int, prerequisites [][]int) bool {
	adjacencies := make(map[int][]int)

	for i := range numCourses {
		adjacencies[i] = make([]int, 0)
	}
	for _, adjacency := range prerequisites {
		adjacencies[adjacency[1]] = append(adjacencies[adjacency[1]], adjacency[0])
	}

	visited := make(map[int]bool)

	for k := range numCourses {
		completable := dfs(k, adjacencies, &visited)

		if completable == false {
			return false
		}
	}

	return true
}
