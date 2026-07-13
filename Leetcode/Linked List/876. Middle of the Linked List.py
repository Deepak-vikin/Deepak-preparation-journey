"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=head
        right=head
        while right and right.next:
            left=left.next
            right=right.next.next
        return left
obj=Solution()
res=obj.middleNode(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
print(res)
