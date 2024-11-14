/*
 * @lc app=leetcode id=1170 lang=golang
 *
 * [1170] Compare Strings by Frequency of the Smallest Character
 */

// @lc code=start
func f(s string) int {
	buckets := [26]int{}
	for _, letter := range s {
		index := letter - 'a'
		buckets[index]++
	}
	for _, bucket := range buckets {
		if bucket != 0 {
			return bucket
		}
	}
	return -1
}
func numSmallerByFrequency(queries []string, words []string) []int {
	largestWord := -1
	for _, word := range words {
		largestWord = max(largestWord, len(word))
	}
	wordFs := make([]int, largestWord+1)
	for _, word := range words {
		wordF := f(word)
		for i := 0; i < wordF; i++ {
			wordFs[i]++
		}
	}
	fmt.Println(wordFs)
	res := make([]int, len(queries))
	for i, query := range queries {
		res[i] = wordFs[f(query)]
	}
	return res
}

// @lc code=end

