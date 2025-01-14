func digitCount(num string) bool {
    counts := make(map[int]int)

    for _, digit := range num {
        parsed, _ := strconv.Atoi(string(digit))
        counts[parsed]++
    }

    for i, digit := range num {
        parsed, _ := strconv.Atoi(string(digit))
        if counts[i] != parsed {
            return false
        }
    }

    return true
}
