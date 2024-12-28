func percentageLetter(s string, letter byte) int {
    var count float64 = 0

    for _, val := range s {
        if byte(val) == letter {
            count++
        }
    }
    return int(math.Floor(count / float64(len(s)) * 100))
}
