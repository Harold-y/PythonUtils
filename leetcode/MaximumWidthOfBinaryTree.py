from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)

        def traverse(node, level, column):
            if node:
                di[level].append(column)
                traverse(node.left, level + 1, column * 2)
                traverse(node.right, level + 1, column * 2 + 1)
        traverse(root, 0, 0)
        return max(max(di[level]) - min(di[level]) + 1 for level in di)


if __name__ == '__main__':
    print(pow(2, 0))
