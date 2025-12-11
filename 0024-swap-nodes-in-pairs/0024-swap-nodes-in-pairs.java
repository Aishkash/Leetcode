class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to simplify handling the head swap
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;

        // Traverse the list in pairs
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = prev.next.next;

            // Swapping the nodes
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Moving prev pointer ahead by two nodes
            prev = first;
        }

        return dummy.next;
    }
}