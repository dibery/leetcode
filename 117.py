class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes, pos = [root, None], 0
        if not root:
            return root
        while pos < len(nodes):
            if nodes[pos] is None:
                if pos != len(nodes) - 1:
                    nodes.append(None)
            else:
                if (n := nodes[pos].left):
                    nodes.append(n)
                if (n := nodes[pos].right):
                    nodes.append(n)
            pos += 1
        for i in range(len(nodes)):
            if nodes[i]:
                nodes[i].next = nodes[i + 1]
        return root
