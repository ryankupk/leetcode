// https://leetcode.com/problems/uncommon-words-from-two-sentences

import (
	// "fmt"
	"strings"
)

func uncommonFromSentences(s1 string, s2 string) []string {
	words1 := strings.Split(s1, " ")
	words2 := strings.Split(s2, " ")

	wordSet1 := make(map[string]int)
	wordSet2 := make(map[string]int)

	unique := []string{}

	for _, word := range words1 {
		wordSet1[word] += 1
	}
	for _, word := range words2 {
		wordSet2[word] += 1
	}

	for _, word := range words1 {
		if wordSet2[word] == 0 && wordSet1[word] <= 1 {
			unique = append(unique, word)
		}
	}
	for _, word := range words2 {
		if wordSet1[word] == 0 && wordSet2[word] <= 1{
			unique = append(unique, word)
		}
	}

	return unique
}
