class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        create = {id(head): Node(head.val) if head else None}
        ret = mod = create[id(head)]
        while head:
            mod.val = head.val
            mod.next = create.setdefault(id(head.next), Node(head.next.val) if head.next else None)
            mod.random = create.setdefault(id(head.random), Node(head.random.val) if head.random else None)
            head = head.next
            mod = mod.next
        return ret
