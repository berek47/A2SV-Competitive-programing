# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        n = len(traversal)
        depth = 0
        i = 0
        while i < n:
            if traversal[i].isdigit():
                start = i
                i += 1
                while i < n and traversal[i].isdigit():
                    i += 1
                while stack and stack[-1][0] >= depth:
                    stack.pop()
                number = int(traversal[start:i])
                newNode = TreeNode(number)
                if stack:
                    parent = stack[-1][1]
                    if parent.left is not None:
                        parent.right = newNode
                    else:
                        parent.left = newNode
                stack.append((depth, newNode))
                depth = 0
            else:
                depth += 1
                i += 1
        
        return stack[0][1] if stack else None
