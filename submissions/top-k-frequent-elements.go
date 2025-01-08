func topKFrequent(nums []int, k int) []int {
    freqs := make([][]int, len(nums)+1)
    counts := make(map[int]int)

    for _, val := range nums {
        counts[val]++
    }

    for val, count := range counts {
        freqs[count] = append(freqs[count], val)
    }

    res := make([]int, k)

    outer:
    for i := len(freqs) - 1; i >= 0; i-- {
        for _, val := range freqs[i] {
            if k == 0 {
                break outer
            }
            res[k-1] = val
            k--
        }
    }
    return res
}
