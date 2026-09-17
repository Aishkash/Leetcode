# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        a=right-left
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(1,left):
            prev = prev.next

        # Start reversing from curr
        curr = prev.next
        for _ in range(a):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return dummy.next    

      