class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        val = []
        h = head
        while h:
            val.append(h.val)
            h = h.next
        val[k - 1], val[-k] = val[-k], val[k - 1]
        h = head
        for v in val:
            h.val = v
            h = h.next
        return head