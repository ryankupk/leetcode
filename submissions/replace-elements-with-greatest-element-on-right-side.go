func replaceElements(arr []int) []int {
    res := make([]int, len(arr))
    res[len(res)-1] = -1
    largest := arr[len(arr)-1]
    for i := len(arr)-2; i >= 0; i-- {
        largest = max(arr[i+1], largest)
        res[i] = largest
    }
    return res
}
