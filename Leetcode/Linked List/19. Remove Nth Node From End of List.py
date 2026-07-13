"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=head
        right=head
        if head.next==None:
            head=None
            return head
        for i in range(n):
            right=right.next
        if right is None:
            return head.next
        while right and right.next:
            left=left.next
            right=right.next
        left.next=left.next.next
        return head
obj=Solution()
res=obj.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2)
print(res)