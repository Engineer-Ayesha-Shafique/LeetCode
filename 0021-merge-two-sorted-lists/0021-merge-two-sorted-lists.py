class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type A: Optional[ListNode]
        :type B: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        current = dummy

        # Iterate through both lists until one of them is exhausted
        while A is not None and B is not None:
            # Compare values of the current nodes in both lists
            if A.val < B.val:
                current.next = A
                A = A.next
            else:
                current.next = B
                B = B.next

            # Move the current pointer to the newly added node
            current = current.next

        # If one of the lists is not exhausted, append the remaining nodes
        if A is not None:
            current.next = A
        elif B is not None:
            current.next = B

        # Return the merged list starting from the dummy node's next
        return dummy.next