class FindElements:

    def __init__(self, root: TreeNode):
        self.val = set()
        self.dfs(root, 0)
            
    def dfs(self, node, val):
        node.val = val
        self.val.add(val)
        if node.left:
            self.dfs(node.left, val * 2 + 1)
        if node.right:
            self.dfs(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.val
