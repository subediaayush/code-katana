# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
# is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
from ListNode import *



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        
        reversed = ListNode()
        buffer = reversed
        buffer.next = head
        
        while(buffer.next):
            startNode = buffer
            for i in range(k - 1):
                nextNode = buffer.next
                
                if not buffer: 
                    break
            endNode = buffer
            savedNode = startNode
            if not end: 
                break

            print('Swapping {} with {}'.format(start, end))
            swap(start, end)
            print('After Swapping {} with {}'.format(start, end))
            # print(reversed)
            buffer = end.next
        return reversed.next

list = listNode([1,2,3,4,5,6,7,8,9])
swap(list.next.next, list.next.next.next)
print(list)
# print(Solution().reverseKGroup(list, 2))
        