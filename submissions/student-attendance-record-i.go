/*
 * @lc app=leetcode id=551 lang=golang
 *
 * [551] Student Attendance Record I
 */

// @lc code=start
func checkRecord(s string) bool {
	absences := 0
	consecutive := 0

	for _, letter := range s {
		if letter == 'P' {
			consecutive = 0
		} else if letter == 'A' {
			absences++
			consecutive = 0
			if absences == 2 {
				return false
			}
		} else if letter == 'L' {
			consecutive++
			if consecutive == 3 {
				return false
			}
		}
	}

	return true
}

// @lc code=end

