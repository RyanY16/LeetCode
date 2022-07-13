# Definition for a binary tree node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getMaxDepth(node):
            if not node:
                return 0
            left = getMaxDepth(node.left)
            right = getMaxDepth(node.right)
            return 1 + max(left, right)
        return getMaxDepth(root)