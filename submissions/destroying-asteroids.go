package main

/*
 * @lc app=leetcode id=2126 lang=golang
 *
 * [2126] Destroying Asteroids
 */

// @lc code=start
import (
	"slices"
)

func asteroidsDestroyed(mass int, asteroids []int) bool {
	slices.Sort(asteroids)

	for _, asteroid := range asteroids {
		if asteroid <= mass {
			mass += asteroid
		} else {
			return false
		}
	}

	return true
}

// @lc code=end
