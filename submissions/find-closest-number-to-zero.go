func abs(x int) int {
    if x < 0 {
        return -1 * x
    }
    return x
}
func findClosestNumber(nums []int) int {
    closest := 100001
    for _, num := range nums {
        cur := abs(num)
        if cur < abs(closest) {
            closest = num
        } else if cur == abs(closest) {
            closest = max(closest, num)
        }
    }

    return closest
}
