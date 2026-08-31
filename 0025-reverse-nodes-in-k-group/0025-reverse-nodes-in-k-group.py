class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while True:

            kth = prev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            next_group = kth.next

            # Reverse k nodes
            curr = prev.next
            prev_node = next_group

            while curr != next_group:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp

            # Connect previous group to reversed group
            temp = prev.next
            prev.next = kth
            prev = temp