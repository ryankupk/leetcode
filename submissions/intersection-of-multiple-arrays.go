import "slices"
func intersection(nums [][]int) []int {
    counts := make(map[int]int)
    n := len(nums)
    
    for _, list := range nums {
        for _, val := range list {
            counts[val]++
        }
    }
    
    res := []int{}
    for k, v := range counts {
        if v == n {
            res = append(res, k)
        }
    }

    slices.Sort(res)
    return res
}
