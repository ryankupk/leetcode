/*
 * @lc app=leetcode id=567 lang=golang
 *
 * [567] Permutation in String
 */

// @lc code=start
func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	n := len(s1)
	s1Map := make(map[rune]int)
	for _, letter := range s1 {
		s1Map[letter]++
	}

	for i := 0; i < len(s2)-n+1; i++ {
		s2Substring := s2[i : i+n]
		s2SubstringMap := make(map[rune]int)

		for _, letter := range s2Substring {
			s2SubstringMap[letter]++
		}
		allSame := true
		for letter, s1Count := range s1Map {
			s2Count, ok := s2SubstringMap[letter]
			if !ok {
				allSame = false
				break
			}
			if s1Count != s2Count {
				allSame = false
				break
			}
		}
		if !allSame {
			continue
		}
		return true
	}

	return false
}

// @lc code=end

