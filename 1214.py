class Solution:
    def BST2List(self, node: TreeNode):
        return (self.BST2List(node.left) if node.left else []) + [node.val] + (node.BST2List(node.right) if node.right else [])
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        a, b = set(self.BST2List(root1)), set(self.BST2List(root2))
        for i in a:
            if target - a in b:
                return True
        return False
