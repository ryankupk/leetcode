func smallestEqual(nums []int) int {
    for i, val := range nums {
        if i % 10 == val {
            return i
        }
    }
    return -1
}
