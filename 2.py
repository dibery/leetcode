class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get(node):
            n = ''
            while node != None:
                n += str(node.val)
                node = node.next
            return int(n[::-1])
        s = map(int, str(get(l1) + get(l2)))
        ans = ListNode(next(s))
        try:
            while True:
                new = ListNode(next(s))
                new.next = ans
                ans = new
        except:
            pass
        return ans
