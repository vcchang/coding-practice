# Univalued binary tree
# (a binary tree is univalued if every node in 
# the tree has the same value)

# Input: Node root

# Depth-first (DFS) recursive approach
# Time: O(n)  -> in worst case, tree is a straight
#                line with n-1 height (recall root
#                is level 0) -> O(n-1) ~= O(n)
# Space: O(n) -> call stack can only grow as tall as 
#                the max depth of the tree -> 
#                n-1 (height) <= depth <= log2(n);
#                therefore, max memory consumed is
#                O(n-1) ~= O(n)

from node import Node
    
def isUnivalued(root: Node):
    nodeVals = []

    def dfs(root: Node):
        if root:
            nodeVals.append(root.val)
            dfs(root.left)
            dfs(root.right)
    
    dfs(root)
    return all(val == nodeVals[0] for val in nodeVals)

if __name__ == "__main__":
    rootNone = None
    expectedNone = True
    actualNone = isUnivalued(rootNone)
    assert actualNone == expectedNone
    print(f"Awesome, we found ourselves a univalued tree: {rootNone}")

    rootOne = Node(1)
    expectedOne = True
    actualOne = isUnivalued(rootOne)
    assert actualOne == expectedOne
    print("Awesome, we found ourselves a univalued tree: [1]")

    rootAllSame = Node(1)
    rootAllSame.left = Node(1)
    rootAllSame.right = Node(1)
    rootAllSame.left.left = Node(1)
    expectedAllSame = True
    actualAllSame = isUnivalued(rootAllSame)
    assert actualAllSame == expectedAllSame
    print("Awesome, we found ourselves a univalued tree: [1, 1, 1, 1]")

    rootNotAllSame = Node(1)
    rootNotAllSame.left = Node(1)
    rootNotAllSame.right = Node(1)
    rootNotAllSame.left.right = Node(2)
    expectedNotAllSame = False
    actualNotAllSame = isUnivalued(rootNotAllSame)
    assert actualNotAllSame == expectedNotAllSame
    print("No univalued tree here: [1, 1, 1, None, 2]")

    rootDeep = Node(1)
    rootDeep.left = Node(1)
    rootDeep.right = Node(1)
    rootDeep.left.left = None
    rootDeep.left.right = Node(1)
    rootDeep.right.left = Node(1)
    rootDeep.right.right = None
    rootDeep.left.right.left = Node(1)
    rootDeep.left.right.right = None
    expectedDeep = True
    actualDeep = isUnivalued(rootDeep)
    assert actualDeep == expectedDeep
    print("Awesome, we found ourselves a univalued tree: [1, 1, 1, None, 1, 1, None, None, None, 1, None]")

    rootDeepNotAllSame = Node(1)
    rootDeepNotAllSame.left = Node(1)
    rootDeepNotAllSame.right = Node(1)
    rootDeepNotAllSame.left.left = None
    rootDeepNotAllSame.left.right = Node(1)
    rootDeepNotAllSame.right.left = Node(1)
    rootDeepNotAllSame.right.right = None
    rootDeepNotAllSame.left.right.left = Node(9)
    expectedDeepNotAllSame = False
    actualDeepNotAllSame = isUnivalued(rootDeepNotAllSame)
    assert actualDeepNotAllSame == expectedDeepNotAllSame
    print(f"No univalued tree here: [1, 1, 1, None, 1, 1, None, None, None, 9]")