# Range sum BST
# Given the root node of a binary search tree, 
# return the sum of values of all nodes with 
# value between L and R (inclusive).

# Assumption: bst is guaranteed to have unique values

# Input: Node bst (with n nodes), int left, int right

# Time: O(n)  -> worst case = linear tree, height = n-1
# Space: O(n) -> call stack will only grow as tall as 
#                max depth (ie: height) of tree -> height
#                = n-1 = tallest tree

from node import Node

def sum(bst: Node, left: int, right: int):
    if not bst:
        return 0
    sumSoFar = 0
    if left <= bst.val <= right:
        sumSoFar += bst.val
    if bst.val > left or bst.val > right:
        sumSoFar += sum(bst.left, left, right)
    if bst.val < right or bst.val < left:
        sumSoFar += sum(bst.right, left, right)
    return sumSoFar

if __name__ == "__main__":
    bstNone = None
    leftNone = 1
    rightNone = 17
    expectedNone = 0
    actualNone = sum(bstNone, leftNone, rightNone)
    assert actualNone == expectedNone
    print(f"Range of sum in bst None = {actualNone}")

    bstOne = Node(1)
    leftOne = -1
    rightOne = 2
    expectedOne = 1
    actualOne = sum(bstOne, leftOne, rightOne)
    assert actualOne == expectedOne
    print(f"Range of sum in bst [1] = {actualOne}")

    bstComplex = Node(10)
    bstComplex.left = Node(4)
    bstComplex.right = Node(17)
    bstComplex.left.left = Node(2)
    bstComplex.left.right = Node(6)
    bstComplex.right.left = Node(13)
    bstComplex.right.right = Node(21)
    bstComplex.right.right.left = Node(19)
    leftComplex = 6
    rightComplex = 19
    expectedComplex = 6 + 10 + 13 + 17 + 19
    actualComplex = sum(bstComplex, leftComplex, rightComplex)
    assert actualComplex == expectedComplex
    print(f"Range of sum in bst [10, 4, 17, 2, 6, 13, 21, None, None, None, None, None, None, 19, None] = {actualComplex}")