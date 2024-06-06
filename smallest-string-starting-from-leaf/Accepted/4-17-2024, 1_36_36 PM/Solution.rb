# https://leetcode.com/problems/smallest-string-starting-from-leaf

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {String}

def convert_to_letter(num)
  # Check if the number is within the valid range for lowercase letters
  if num >= 0 && num <= 25
    # Add the ASCII code for 'a' to the number to get the corresponding letter
    (num + 97).chr
  else
    # Return an empty string or handle the case where the number is out of range
    raise Exception
  end
end

def traverse(node, substr, strs) 
    if node.left.nil? and node.right.nil?
        # p convert_to_letter(node.val) + substr.reverse
        strs << (convert_to_letter(node.val) + substr)
    elsif node.left.nil? and !node.right.nil?
        traverse(node.right, convert_to_letter(node.val) + substr, strs)
    elsif !node.left.nil? and node.right.nil?
        traverse(node.left, convert_to_letter(node.val) + substr, strs)
    else
        traverse(node.left , convert_to_letter(node.val) + substr, strs)
        traverse(node.right, convert_to_letter(node.val) + substr, strs)
    end
end

def smallest_from_leaf(root)
    smallest = 'z' * 8500
    strs = []
    traverse(root, '', strs)
    # p "traversed:"
    # p strs
    strs.min
end