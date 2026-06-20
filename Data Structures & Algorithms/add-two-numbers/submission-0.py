# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        
        
        l1_list = l1_list[::-1]
        l2_list = l2_list[::-1]

        print(l1_list)
        print(l2_list)

        num_1 = ''
        num_2 = ''
        for i in l1_list:
            num_1 = num_1+str(i)

        for i in l2_list:
            num_2 = num_2+str(i)
        
        print(num_1)
        print(num_2)

        total = int(num_1)+int(num_2)
        
        final_val= []

        for i in range(0,len(str(total))):
            final_val.append(str(total)[i])

        final_val = final_val[::-1]
        print(final_val)

        head = curr = ListNode(0)
        for i in final_val:
            curr.next = ListNode(int(i))
            curr = curr.next
        
        return head.next
        
        


        