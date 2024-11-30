func distributeCandies(candies int, num_people int) []int {
    
    res := make([]int, num_people)

    idx := 0
    nextCandy := 1
    for candies > 0 {
        if nextCandy < candies {
            res[idx] += nextCandy
        } else {
            res[idx] += candies
            candies = 0
            break
        }
        idx = (idx + 1) % num_people
        candies -= nextCandy
        nextCandy++
    }

    return res
}
