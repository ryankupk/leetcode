/*
 * @lc app=leetcode id=804 lang=golang
 *
 * [804] Unique Morse Code Words
 */

// @lc code=start
func uniqueMorseRepresentations(words []string) int {
	var aRune rune = 'a'
	morse := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	res := make(map[string]bool)
	for _, word := range words {
		morseWord := ""
		for _, letter := range word {
			morseLetter := morse[letter-aRune]
			morseWord += string(morseLetter)
		}

		res[morseWord] = true
	}
	return len(res)
}

// @lc code=end

