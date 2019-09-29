class Solution:
    def __init__(self):
        self.reach, self.left, self.right = [0] * 100, [0] * 100, [0] * 100
    def traverse(self, node):
        if node.left != None:
            self.reach[node.val] = self.traverse(node.left)
            self.left[node.val] = node.left.val
        if node.right != None:
            self.reach[node.val] += self.traverse(node.right)
            self.right[node.val] = node.right.val
        self.reach[node.val] += 1
        return self.reach[node.val]
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.traverse(root)
        if x in self.left:
            p = self.left.index(x)
        elif x in self.right:
            p = self.right.index(x)
        else:
            p = 0
        l, r = self.left[x], self.right[x]
        return max(n - self.reach[x], self.reach[l], self.reach[r]) > n / 2
