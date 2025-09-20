class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = Node(0)
        dummy.next = head
        pre = dummy
        curr = head

        while curr:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    pre.next = curr
                    return dummy.next
            
            next_group = tail.next

            # Reverse the sublist
            prev_rev = next_group
            curr_rev = curr
            while curr_rev != next_group:
                next_node = curr_rev.next
                curr_rev.next = prev_rev
                prev_rev = curr_rev
                curr_rev = next_node

            pre.next = prev_rev
            pre = curr
            curr = next_group
        
        return dummy.next
