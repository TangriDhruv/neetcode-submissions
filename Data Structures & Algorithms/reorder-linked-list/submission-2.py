# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #[2,4,6,8]
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        curr = head2
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        first = head
        second = head2

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2

            


        