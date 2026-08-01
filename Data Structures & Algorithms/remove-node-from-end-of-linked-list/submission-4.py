# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length=0

        curr=head

        while curr:

            length+=1

            curr=curr.next

        pos=length-n

        if length==1:

            return ListNode("")

        if pos==0:

            return head.next

        length=0

        curr=head

        temp,conn=None,None

        while curr:

            if length==pos-1:

                temp=curr.next

                conn=temp.next

                curr.next=conn

            length+=1

            curr=curr.next

        return head




        