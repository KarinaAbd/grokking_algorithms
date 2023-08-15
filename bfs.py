from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
# to the farthest leaf node.
def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()
        level += 1

        if node.left:
            queue.append((node.left, level))
        if node.right:
            queue.append((node.right, level))

    return level


assert maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 3
assert maxDepth(TreeNode(1, None, TreeNode(2))) == 2


# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down 
# to the nearest leaf node.
def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
        
    queue = deque()
    queue.append((root, 1))

    while queue:
        node, level = queue.popleft()

        if not node.left and not node.right:
            return level
                
        level += 1
        if node.left:
            queue.append((node.left, level))
        if node.right:
            queue.append((node.right, level))
    return level


assert minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 2
assert minDepth(TreeNode(1, None, TreeNode(2))) == 2
