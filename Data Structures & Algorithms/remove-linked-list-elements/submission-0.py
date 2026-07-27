# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy=ListNode(0)

        temp=dummy

        curr=head

        while curr:

            if curr.val!=val:

                temp.next=ListNode(curr.val)

                temp=temp.next

            curr=curr.next

        return dummy.next



            


        