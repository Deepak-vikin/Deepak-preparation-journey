"""
Given a linked list with the head node and a key, the task is to check if the key is present in the linked list or not. Return true if key is present, else return false.

Example:

Input: key = 3,

Output: true
Explanation: 3 is present in Linked List.
"""

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def searchKey(self, head, key):
        if head == None:
            return False
        if head.data == key:
            return True
        temp = head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
obj=Solution()
res=obj.searchKey(3,3)
print(res)