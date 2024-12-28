func maxPower(s string) int {
    power := make([]int, len(s))
    var prev rune = rune(s[0])
    power[0] = 1
    highest := 1
    for i, val := range s[1:] {
        if val == prev {
            power[i+1] = power[i] + 1
            highest = max(highest, power[i+1])
        } else {
            prev = val
            power[i+1] = 1
        }
    }
    return highest
}
