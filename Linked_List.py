# Creating and printing Linked List

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=Node

#     def displayLinkedlist(self):
#         curr=self.head
#         while curr:
#             print(curr.data,end="->")
#             curr=curr.next

#         print("None")


# ll=Linkedlist()

# Node1=Node(10)
# Node2=Node(20)
# Node3=Node(30)

# ll.head=Node1
# ll.head.next=Node2
# Node2.next=Node3

# ll.displayLinkedlist()

# Reverse Linked List
# optimal solution
# Time complexity=O(n)
# Space complexity=O(1)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def reverse_linked_list(head):
#     prev=None
#     curr=head

#     while curr:
#         nxt=curr.next
#         curr.next=prev
#         prev=curr
#         curr=nxt

#     return prev

# def display_Linked_List(head):
#     temp=head
#     while temp:
#         print(temp.data,end="->")
#         temp=temp.next

#     print("None")
    

# Node1=Node(10)
# Node2=Node(20)
# Node3=Node(30)

# Node1.next=Node2
# Node2.next=Node3

# display_Linked_List(Node1)

# reverse_ll=reverse_linked_list(Node1)
# display_Linked_List(reverse_ll)



