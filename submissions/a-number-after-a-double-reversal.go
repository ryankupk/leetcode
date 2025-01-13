func isSameAfterReversals(num int) bool {
    str := strconv.Itoa(num)
    if str == "0" {
        return true
    }
    return str[len(str)-1] != '0'
}
