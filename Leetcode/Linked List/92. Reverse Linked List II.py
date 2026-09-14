"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        temp = head
        before_start = None
        start = None
        end = None
        after_end = None
        prev = None
        while temp:
            if index == left:
                before_start = prev
                start = temp
            if index == right:
                after_end = temp.next
                end = temp
            index += 1
            prev = temp
            temp = temp.next
        temp = start
        prev = None
        while temp and temp != after_end:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        if before_start:
            before_start.next = prev
        else:
            head = prev
        start.next = after_end
        return head
obj=Solution()
res=obj.reverseBetween([1,2,3,4,5],1,,2)
print(res)







