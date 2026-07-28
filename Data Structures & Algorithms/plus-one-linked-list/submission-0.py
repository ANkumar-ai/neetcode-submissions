# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        #Let's say you add the ctr till the end, and in the end 

        curr=head
        
        temp=ListNode(0)

        dummy=temp

        sample=[]

        while curr:

            sample.append(str(curr.val))

            curr=curr.next

        num = int("".join(sample))
        num += 1
        
        maxl=str(num)

        for i in range(len(maxl)):

            dummy.next=ListNode(int(maxl[i]))

            dummy=dummy.next

        return temp.next


