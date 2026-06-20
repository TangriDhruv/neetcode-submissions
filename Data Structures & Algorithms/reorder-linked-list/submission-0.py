# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle node:
        # Revese the second half of the node
        # combine them one after another

        # 1. Find the middle node:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # 2. Reverse the head2 list:
        curr = head2
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        # 3. Alternate head1 and head2
        first = head 
        second = head2 
        dummy = node = first 
        #head = [0,1,2,3]
        #head2 = [6,5,4]
        first, second = head, head2
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        