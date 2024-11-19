package main

import "fmt"

/*
 * @lc app=leetcode id=911 lang=golang
 *
 * [911] Online Election
 */

// @lc code=start
type TopVotedCandidate struct {
	Persons            []int
	Times              []int
}

func Constructor(persons []int, times []int) TopVotedCandidate {
	return TopVotedCandidate{Persons: persons, Times: times}
}

// [0, 1, 1 , 0 , 0 , 1 , 0 ]
// [0, 5, 10, 15, 20, 25, 30]
// [3,12, 25, 15, 24, 8     ]

func (this *TopVotedCandidate) Q(t int) int {

	// candidateVotesMap := make(map[int]int)
	candidateVotesMap := [5000]int{}
	currentLeader := -1
	currentHighest := -1

	for i, person := range this.Persons {
		if this.Times[i] <= t {
			candidateVotesMap[person]++
			if candidateVotesMap[person] >= currentHighest {
				currentHighest = candidateVotesMap[person]
				currentLeader = person
			}
			continue
		}
		// fmt.Printf("Reached time %d\n%v\n%d\n", this.Times[i], candidateVotesMap, currentLeader)
		return currentLeader
	}

	return currentLeader
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * obj := Constructor(persons, times);
 * param_1 := obj.Q(t);
 */
// @lc code=end
