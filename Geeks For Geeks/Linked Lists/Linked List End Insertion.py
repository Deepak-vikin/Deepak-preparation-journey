"""
You are given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the head of the modified Linked List.

Examples :

Input: x = 6,

Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Explanation: We can see that 6 is inserted at the end of the linkedlist.
"""

'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        newnode=Node(x)
        if head==None:
            head=newnode
            return head
        if head.next==None:
            head.next=newnode
            return head
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        return head
obj=Solution()
res=obj.insertAtEnd(Node(1),6)
print(res.data)