func numberOfPairs(nums []int) []int {
    counts := make(map[int]int)

    for _, num := range nums {
        counts[num]++
    }

    res := []int{0,0}

    for _, count := range counts {
        res[0] += count / 2
        res[1] += count % 2
    }

    return res
}
