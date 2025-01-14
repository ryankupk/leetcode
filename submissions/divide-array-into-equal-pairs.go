func divideArray(nums []int) bool {
    counts := make(map[int]int)

    for _, num := range nums {
        counts[num]++
    }

    for _, v := range counts {
        if v % 2 != 0 {
            return false
        }
    }

    return true
}
