/*
 * @lc app=leetcode id=2490 lang=golang
 *
 * [2490] Circular Sentence
 */

// @lc code=start
import (
	"strings"
)

func isCircularSentence(sentence string) bool {
	if sentence[0] != sentence[len(sentence)-1] {
		return false
	}

	splitSentence := strings.Split(sentence, " ")

	if len(splitSentence) == 2 {
		word, nextWord := splitSentence[0], splitSentence[1]
		return (word[len(word)-1] == nextWord[0]) && (word[0] == nextWord[len(nextWord)-1])
	}

	for i := 1; i < len(splitSentence); i++ {
		word, prevWord := splitSentence[i], splitSentence[i-1]
		if word[0] != prevWord[len(prevWord)-1] {
			return false
		}
	}

	return true
}

// @lc code=end

