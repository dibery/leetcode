class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth=0):
            if node is None:
                return (-1, 0)
            l, r = dfs(node.left, depth + 1), dfs(node.right, depth + 1)
            if l[0] == r[0]:
                return (l[0], l[1] + r[1]) if ~l[0] else (depth, node.val)
            return max(l, r)
        return dfs(root)[1]
