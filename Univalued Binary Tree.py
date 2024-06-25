# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        q = [root]
        while(q):
            x = q.pop(0)
            if x.val != val:
                return False 
            if x.left :
                q.append(x.left)
            if x.right:
                q.append(x.right)
        return True
