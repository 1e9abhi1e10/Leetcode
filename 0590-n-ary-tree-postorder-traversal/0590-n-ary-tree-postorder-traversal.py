"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root, output):
            if not root:
                return None
           # output.append(root.val)
            for child in root.children:
                dfs(child, output)
            output.append(root.val)
            return output
        
        return dfs(root, [])