# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root.val if root else None)
        # if not root or not root.left: return root
        if not root: return 
        # if not root.left.left:
        #     tmp = root.left 
        #     root.left = root.right
        #     root.right = tmp
        #     return root
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root






        # print(root.val)
        # if not root: return root
        # if not root.left.left: 
        #     tmp = root.left 
        #     root.left = root.right
        #     root.right = tmp
        #     return root
        # root = self.invertTree(root.right)
        # root = self.invertTree(root.left)
        # return root