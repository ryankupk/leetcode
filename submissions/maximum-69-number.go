import (
    "strconv"
    "strings"
)
func maximum69Number (num int) int {
    str := strconv.Itoa(num)
    split := strings.Split(str, "")
    for i, val := range split {
        if val == "6" {
            split[i] = "9"
            break
        }
    }
    x, _ := strconv.Atoi(strings.Join(split, ""))
    return x
}
