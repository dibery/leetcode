class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if node.val == target.val:
                return node
            if node.left and (l := dfs(node.left)):
                return l
            if node.right:
                return dfs(node.right)
        return dfs(cloned)
