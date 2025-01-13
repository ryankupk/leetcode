func countPoints(rings string) int {
    rods := make([]map[byte]bool, 10)
    for i := range rods {
        rods[i] = make(map[byte]bool)
    }
    
    for i := 0; i < len(rings); i += 2 {
        color := rings[i]
        rod, _ := strconv.ParseInt(string(rings[i+1]), 10, 32)
        rods[rod][color] = true
    }

    res := 0
    for _, rod := range rods {
        if len(rod) == 3 {
            res++
        }
    }
    
    return res
}
