func maxNumberOfBalloons(text string) int {
    counts := make(map[rune]int)

    for _, letter := range text {
        counts[letter]++
    }

    return min(counts['b'], min(counts['a'], min(counts['l']/2, min(counts['o']/2, min(counts['n'])))))
}
