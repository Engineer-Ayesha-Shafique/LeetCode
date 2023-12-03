# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Initialize two pointers
        slow = head
        fast = head

        # Traverse the linked list
        while fast and fast.next:
            slow = slow.next  # Move one step
            fast = fast.next.next  # Move two steps

            # Check if the two pointers meet
            if slow == fast:
                return True  # There is a cycle

        # If the loop completes, there is no cycle
        return False
