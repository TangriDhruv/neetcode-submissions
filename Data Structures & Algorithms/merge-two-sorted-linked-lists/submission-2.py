# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if not list1 and not list2:
            return None
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next
        
        arr = sorted(arr)
        head = node = ListNode(arr[0])
        for i in range(1,len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

        