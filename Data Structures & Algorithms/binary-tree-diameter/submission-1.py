# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def thmx(root) -> int:
            nonlocal maxi

            if not root: return 0
            l = thmx(root.left)
            r = thmx(root.right)
            sum3 = l + r
            maxi = max(maxi, sum3)
            return 1 + max(l, r)
        thmx(root)
        return maxi