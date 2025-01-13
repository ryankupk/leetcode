func maxDistance(colors []int) int {
    largestDistance := -1

    l, r := 0, len(colors) - 1

    for colors[l] == colors[r] {
        r--
    }
    largestDistance = max(r - l, largestDistance)

    l, r = 0, len(colors) - 1

    for colors[l] == colors[r] {
        l++
    }
    largestDistance = max(r - l, largestDistance)

    return largestDistance
}
