/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import (
    "math/rand/v2"
)
// type Solution struct {
//     Head *ListNode
//     Length int
// }
type Solution struct {
    List []int
}

// func Constructor(head *ListNode) Solution {
//     length := 0
//     save := head

//     for head != nil {
//         length++
//         head = head.Next
//     }
//     return Solution{Head: save, Length: length}
// }
func Constructor(head *ListNode) Solution {
    list := []int{}
    for head != nil {
        list = append(list, head.Val)
        head = head.Next
    }
    return Solution{List: list}
}

// func (this *Solution) GetRandom() int {
//     save := this.Head
//     idx := rand.IntN(this.Length)
//     for i := 0; i < idx; i++ {
//         this.Head = this.Head.Next
//     }
//     res := this.Head.Val
//     this.Head = save
//     return res
// }
func (this *Solution) GetRandom() int {
    idx := rand.IntN(len(this.List))
    return this.List[idx]
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
