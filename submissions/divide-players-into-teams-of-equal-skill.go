// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

import (
	"sort"
	"fmt"
)

func dividePlayers(skill []int) int64 {

	sort.Ints(skill)
	n := len(skill) / 2

	var chemistry int64 = 0
	var neededChemistry int64 = int64(skill[0]) + int64(skill[len(skill)-1])
	// fmt.Println(neededChemistry)

	for i := 0; i < n; i++ {
		currentChemistry := (int64(skill[i]) + int64(skill[len(skill)-i-1]))
		// fmt.Println(currentChemistry)
		if currentChemistry != neededChemistry {
			return int64(-1)
		}
		chemistry += (int64(skill[i]) * int64(skill[len(skill)-i-1]))

	}

	return chemistry
}
