# Big O(n) time for iterating through linked list | space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nextNode = curr.next

            if curr.val == val:
                prev.next = nextNode
            else:
                prev = curr

            curr = nextNode

        return dummy.next
