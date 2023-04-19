from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, curr_num, direction):
        if node is None:
            return curr_num
        if direction is True:  # GO TO Left in this turn
            return max(self.dfs(node.left, curr_num + 1, False), self.dfs(node.right, 0, True))
        else:
            return max(self.dfs(node.right, curr_num + 1, True), self.dfs(node.left, 0, False))

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root, -1, True), self.dfs(root, -1, False))
