class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        start=end=head
        while start and start.next:
            end=end.next
            start=start.next.next
        
        prev=None
        while end:
            a=end.next
            end.next=prev
            prev=end
            end=a

        left=head
        right=prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
        