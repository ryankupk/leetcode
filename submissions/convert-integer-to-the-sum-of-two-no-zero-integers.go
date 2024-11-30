import (
    "strconv"
)

func hasZero(a int) bool {
    x := strconv.Itoa(a)
    for _, letter := range x {
        if letter == '0' {
            return true
        }
    }
    return false
}

func getNoZeroIntegers(n int) []int {
    a, b := n-1, 1
    for hasZero(a) || hasZero(b) {
        a--
        b++
    }

    return []int{a, b}
}
