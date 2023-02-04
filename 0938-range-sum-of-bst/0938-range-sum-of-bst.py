# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stk = [root]
        ans = 0 
        while stk:
            node = stk.pop()
            if low<=node.val<=high:
                ans+=node.val
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return ans