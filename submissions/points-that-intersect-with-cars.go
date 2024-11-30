package main

/*
 * @lc app=leetcode id=2848 lang=golang
 *
 * [2848] Points That Intersect With Cars
 */

// @lc code=start

// "sort"

func numberOfPoints(nums [][]int) int {
	buckets := [101]int{}

	for _, carRange := range nums {
		for i := carRange[0]; i <= carRange[1]; i++ {
			buckets[i]++
		}
	}

	res := 0
	for _, num := range buckets {
		if num > 0 {
			res++
		}
	}

	// events := [][]int{} // LSA

	// for _, carRange := range nums {
	// 	events = append(events, []int{carRange[0], 0})
	// 	events = append(events, []int{carRange[1] + 1, 1})
	// }

	// sort.Slice(events, func(i, j int) bool {
	// 	if events[i][0] == events[j][0] {
	// 		return events[i][1] < events[j][1]
	// 	}
	// 	return events[i][0] < events[j][0]
	// })

	// activeCars := 0
	// lastPoint := 0
	// res := 0

	// for _, eventSet := range events {
	// 	point, eventType := eventSet[0], eventSet[1]

	// 	if activeCars > 0 {
	// 		totalCovered += point - lastPoint
	// 	}

	// 	if eventType == 0 {
	// 		activeCars++
	// 	} else {
	// 		activeCars--
	// 	}

	// 	lastPoint = point
	// }

	return res
}

// @lc code=end
