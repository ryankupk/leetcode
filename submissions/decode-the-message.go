func decodeMessage(key string, message string) string {
    encoding := make(map[rune]int)

    idx := 0
    for _, letter := range key {
        if letter == ' ' {
            continue
        }
        if _, ok := encoding[letter]; !ok {
            encoding[letter] = idx
            idx++
        }
    }

    var res strings.Builder

    for _, letter := range message {
        if letter == ' ' {
            res.Write([]byte{' '})
            continue
        }

        res.Write([]byte{byte(encoding[letter] + 'a')})
    }
    return res.String()
}
