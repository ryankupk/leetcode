func minimumLength(s string) int {
    length := 'z'-'a'+1
    counts := make([]int, length)

    res := len(s)

    for _, letter := range s {
        idx := letter-'a'
        counts[idx]++
    }

    for _, count := range counts {
        if count == 0 {
            continue
        }

        if count % 2 == 0 {
            res -= count - 2
        } else {
            res -= count - 1
        }
    }

    return res
}
