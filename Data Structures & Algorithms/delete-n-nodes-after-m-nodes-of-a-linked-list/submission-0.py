# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        dummy=ListNode(0)

        temp_dummy=dummy

        curr=head

        ctr1=0

        while curr:

            if ctr1==m:

                # skip n times

                ctr2=n

                while ctr2 and curr:

                    ctr2-=1

                    curr=curr.next

                ctr2,ctr1=0,0
            
            else: 

                temp_dummy.next=ListNode(curr.val)
                
                temp_dummy=temp_dummy.next

                ctr1+=1
                
                curr=curr.next

        return dummy.next

    








        