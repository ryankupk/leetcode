func isPrefixAndSuffix(wordOne, wordTwo string) bool {
    if len(wordTwo) < len(wordOne) {
        return false
    }
    if len(wordTwo) == len(wordOne) {
        return wordOne == wordTwo
    }

    return wordTwo[:len(wordOne)] == wordOne && wordTwo[len(wordTwo) - len(wordOne):] == wordOne
}

func countPrefixSuffixPairs(words []string) int {
    res := 0
    for i, wordOne := range words {
        for _, wordTwo := range words[i+1:] {
            if isPrefixAndSuffix(wordOne, wordTwo) {
                res++
            }
        }
    }
    return res
}
