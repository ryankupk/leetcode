func flipAndInvertImage(image [][]int) [][]int {
    res := make([][]int, len(image))
    for i := range image {
        res[i] = make([]int, len(image[i]))
    }
    fmt.Println(res)
    for i, row := range image {
        jj := len(row) - 1
        for _, val := range row {
            res[i][jj] = int(math.Abs(float64(val-1))) // invert pixel
            jj--
        }
    }
    
    return res
}
