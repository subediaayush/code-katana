import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        swapped = ListNode()
        r = swapped

        while (head.next):
            first = head
            second = first.next
            third = second.next

            r.next = second
            second.next = first
            first.next = third

            r = r.next.next
            head = head.next.next
            
        return swapped.next