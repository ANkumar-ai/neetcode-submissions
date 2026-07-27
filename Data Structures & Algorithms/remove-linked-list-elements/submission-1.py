# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        temp=head

        prev=ListNode(0)

        temps=prev

        while temp:

            if temp.val!=val:

                temps.next=ListNode(temp.val)

                temps=temps.next


            temp=temp.next

        return prev.next
        