class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return head

        end=start=head
        while start and start.next:
            end=end.next
            start=start.next.next

        sec = end.next
        end.next = None

        prev=None
        while sec:
            a=sec.next
            sec.next=prev
            prev=sec
            sec=a

        left=head
        right=prev
        while right:
            lleft = left.next
            lright = right.next

            left.next = right
            right.next = lleft   

            left = lleft
            right = lright