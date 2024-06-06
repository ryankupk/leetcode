// https://leetcode.com/problems/palindrome-number

# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    x = x.to_s
    left_pointer = 0
    right_pointer = x.length - 1

    is_palindrome = true
    while left_pointer < right_pointer do
        if x[left_pointer] != x[right_pointer]
            is_palindrome = false
            break
        end

        left_pointer += 1
        right_pointer -= 1
    end
    return is_palindrome
end