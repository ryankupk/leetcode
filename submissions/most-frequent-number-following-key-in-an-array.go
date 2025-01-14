func mostFrequent(nums []int, key int) int {
    targets := make(map[int]int)
    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] != key {
            continue
        }

        targets[nums[i+1]]++
    }

    largest, largestCount := -1, -1
    for target, count := range targets {
        if count > largestCount {
            largest = target
            largestCount = count
        }
    }

    return largest
}
