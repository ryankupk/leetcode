func slope(coOne, coTwo []int) float64 {
    num := (float64(coTwo[1]) - float64(coOne[1]))
    den := (float64(coTwo[0]) - float64(coOne[0]))
    if den == 0 {
        return math.Inf(1)
    }
    return num / den
}

func checkStraightLine(coordinates [][]int) bool {
    if len(coordinates) <= 2 {
        return true
    }
    neededSlope := slope(coordinates[0], coordinates[1])
    
    for i, coOne := range coordinates[1:len(coordinates)-1] {
        currentSlope := slope(coOne, coordinates[i+2])
        if currentSlope != neededSlope {
            return false
        }
    }

    return true
}
