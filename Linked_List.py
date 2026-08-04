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


# Merge two sorted list
# optimal solution
# Time complexity=O(M+N)
# Space complexity=O(1)

# class ListNode:
#     def __init__(self,val=0,next=None):

#         self.val=val
#         self.next=next

# def creating_linked_list(arr):
#     head=ListNode(int(arr[0]))
#     curr=head
#     for val in arr[1:]:
#         curr.next=ListNode(int(val))
#         curr=curr.next
#     return head

# def Merge_Linked_List(list1,list2):

#     dummy=ListNode(0)
#     tail=dummy

#     while  list1 and list2:
#         if list1.val<=list2.val:
#             tail.next=list1
#             list1=list1.next

#         else:
#             tail.next=list2
#             list2=list2.next
        
#         tail=tail.next

#     tail.next= list1 if list1 else list2
#     return dummy.next

# def display_Linked_List(head):

#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next

#     print("None")


# l1_input=["1","3","8"]
# l2_input=["4","7","12","17"]

# ll1=creating_linked_list(l1_input)
# ll2=creating_linked_list(l2_input)

# merge=Merge_Linked_List(ll1,ll2)

# print("Merge List:")
# display_Linked_List(merge)


# Linked List cycle
# optimal approach using slow fast pointer
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# def Creating_Linked_List(arr,pos):
#     if not arr:
#         return None

#     head=Node(int(arr[0]))
#     curr = head
#     for val in arr[1:]:
#         curr.next=Node(int(val))
#         curr=curr.next

#     if pos!=-1:
#         target=head
#         for _ in range(pos):
#             target=target.next
#             curr.next=target

#     return head

# def has_cycle(head):
#     slow=head
#     fast=head

#     while fast and fast.next:
#         slow=slow.next
#         fast=fast.next.next

#         if slow==fast:
#             return True

#     return False

# arr=[2,4,7,8,6,1,3]
# pos=2
# ll=Creating_Linked_List(arr,pos)
# print(has_cycle(ll))


# arr=[1,4,6,7]
# pos=-1
# ll=Creating_Linked_List(arr,pos)
# print(has_cycle(ll))

# Reorder list
# optimal solution

class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def Create_Linked_List(arr):
    if not arr:
        return None
    head=Node(int(arr[0]))
    curr=head
    for val in arr[1:]:
        curr.next=Node(int(val))
        curr=curr.next
    return head

def reorder_List(head):

    if not head or not head.next:
        return

    slow=head
    fast=head.next

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    second=slow.next
    slow.next=None

    prev=None
    curr=second

    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt

    second=prev

    first=head
    while second:
        temp1=first.next
        temp2=second.next

        first.next=second
        second.next=temp1

        first=temp1
        second=temp2

    return first

def display_Linked_List(head):

    curr=head
    while curr:
        print(curr.val,end="->")
        curr=curr.next

    print("None")


arr=["1","3","7","9","8","6","2"]
ll=Create_Linked_List(arr)

print("Original List:")
display_Linked_List(ll)


reorder_List(ll)

print("Reordered List:")
display_Linked_List(ll)



    
