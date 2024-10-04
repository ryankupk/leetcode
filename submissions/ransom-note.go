// https://leetcode.com/problems/ransom-note

import (
	"strings"
	"fmt"
)

func canConstruct(ransomNote string, magazine string) bool {
	ransomCount := make(map[rune]int)
	for _, letter := range ransomNote {
		ransomCount[letter]++
	}
	magazineCount := make(map[rune]int)
	for _, letter := range magazine {
		magazineCount[letter]++
	}

	for letter, count := range ransomCount {
		if magazineCount[letter] -= count; magazineCount[letter] < 0 {
			return false
		}
	}

	// fmt.Println(ransomCount)
	// fmt.Println(magazineCount)

	return true
}
