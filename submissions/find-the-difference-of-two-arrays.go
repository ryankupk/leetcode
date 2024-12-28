func findDifference(nums1 []int, nums2 []int) [][]int {
    res := make([][]int, 2)
    setOne, setTwo := make(map[int]bool), make(map[int]bool)

    for _, val := range nums1 {
        setOne[val] = true
    }
    for _, val := range nums2 {
        setTwo[val] = true
    }

    for k := range setOne {
        if !setTwo[k] {
            res[0] = append(res[0], k)
        }
    }
    for k := range setTwo {
        if !setOne[k] {
            res[1] = append(res[1], k)
        }
    }

    return res
}
