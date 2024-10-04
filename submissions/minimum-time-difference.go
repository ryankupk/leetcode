// https://leetcode.com/problems/minimum-time-difference

import (
	"sort"
	"strings"
	"strconv"
	// "fmt"
)

func findMinDifference(timePoints []string) int {

	var timePointInts []int

    for _, timePointStr := range timePoints {
        splitTimePointStr := strings.Split(timePointStr, ":")
        hourConv, _ := strconv.Atoi(splitTimePointStr[0])
        minuteConv, _ := strconv.Atoi(splitTimePointStr[1])
        minutes := 60*hourConv + minuteConv
        timePointInts = append(timePointInts, minutes)
    }
    sort.Ints(timePointInts)

    minDiff := 1440 // Initialize with the maximum possible difference (24 hours)
    for i := 1; i < len(timePointInts); i++ {
        diff := timePointInts[i] - timePointInts[i-1]
        if diff < minDiff {
            minDiff = diff
        }
    }

    // Check the wrap-around case
    wrapAroundDiff := 1440 - (timePointInts[len(timePointInts)-1] - timePointInts[0])
    if wrapAroundDiff < minDiff {
        minDiff = wrapAroundDiff
    }

    return minDiff
}
