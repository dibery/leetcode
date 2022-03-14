class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        val = []
        h = head
        while h:
            val.append(h.val)
            h = h.next
        k %= len(val)
        h = head
        val = val[-k:] + val[:-k]
        print(val)
        i = 0
        while h:
            h.val = val[i]
            i += 1
            h = h.next
        return head
