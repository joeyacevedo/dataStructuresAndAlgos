"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #check to see if there is no head node given
        if not heard: return head
        #placeholder node
        dummy = Node(0)
        #create a current node holder and a stack that includes head
        current, stack = dummy, [head]

        while stack:
            #remove the node in the stack
            temp = stack.pop()

            #possible to write as one line
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)

            current.next = temp
            temp.prev = current
            temp.child = None
            current = temp

        #break the head linkage to dummy
        dummy.next.prev = None

        #return the head node
        return dummy.next
