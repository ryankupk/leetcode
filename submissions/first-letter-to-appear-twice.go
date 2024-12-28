func repeatedCharacter(s string) byte {
    encountered := make(map[rune]bool)

    for _, letter := range s {
        if _, ok := encountered[letter]; ok {
            return byte(letter)
        } else {
            encountered[letter] = true
        }
    }
    return 'a'
}
