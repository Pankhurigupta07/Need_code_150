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
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# def Create_Linked_List(arr):
#     if not arr:
#         return None
#     head=Node(int(arr[0]))
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(int(val))
#         curr=curr.next
#     return head

# def reorder_List(head):

#     if not head or not head.next:
#         return

#     slow=head
#     fast=head.next

#     while fast and fast.next:
#         slow=slow.next
#         fast=fast.next.next

#     second=slow.next
#     slow.next=None

#     prev=None
#     curr=second

#     while curr:
#         nxt=curr.next
#         curr.next=prev
#         prev=curr
#         curr=nxt

#     second=prev

#     first=head
#     while second:
#         temp1=first.next
#         temp2=second.next

#         first.next=second
#         second.next=temp1

#         first=temp1
#         second=temp2

#     return first

# def display_Linked_List(head):

#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next

#     print("None")


# arr=["1","3","7","9","8","6","2"]
# ll=Create_Linked_List(arr)

# print("Original List:")
# display_Linked_List(ll)


# reorder_List(ll)

# print("Reordered List:")
# display_Linked_List(ll)



#Remove Nth Node From End of List
# optimal solution using fast slow pointer
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# def Create_Linked_List(arr):
#     if not arr:
#         return None

#     head=Node(int(arr[0]))
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(int(val))
#         curr=curr.next
#     return head   

# def Remove_nth_node(head,n):

#     dummy=Node(0,head)
#     slow=dummy
#     fast=dummy

#     for _ in range(n+1):
#         fast=fast.next
    
#     while fast:
#         slow=slow.next
#         fast=fast.next

#     slow.next=slow.next.next

#     return dummy.next

# def Display_Linked_List(head):

#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
    
#     print("None")


# arr=["1","4","2","3","7","8","9"]
# n=int(input())

# ll=Create_Linked_List(arr)
# Display_Linked_List(ll)
# modified_ll=Remove_nth_node(ll,n)
# Display_Linked_List(modified_ll)


# copy list with random pointer
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None,random=None):
#         self.val=val
#         self.next=next
#         self.random=random

# def Creating_Linked_List(values,random_indicies):

#     if not values:
#         return None

#     nodes=[Node(val) for val in values]

#     for i in range(len(nodes)-1):
#         nodes[i].next=nodes[i+1]
    
#     for i ,r_idx in enumerate(random_indicies):
#         if r_idx  is not None:
#             nodes[i].random=nodes[r_idx]

#     return nodes[0]

# def Display_Linked_List(head):
    
#     curr=head
#     while curr:
#         random_val=curr.random.val if curr.random else None
#         print(f"[V:{curr.val}|R:{random_val}]",end="->")
#         curr=curr.next

#     print("None")

# def Copy_random_list(head):
#     if not head:
#         return None

#     curr=head
#     while curr:
#         clone=Node(curr.val,curr.next)
#         curr.next=clone
#         curr=clone.next

#     curr=head

#     while curr:
#         if curr.random:
#             curr.next.random=curr.random.next
#         curr=curr.next.next

#     curr=head
#     clone_head=head.next
#     clone_curr=clone_head

#     while curr:
#         curr.next=curr.next.next
#         clone_curr.next=clone_curr.next.next if clone_curr.next else None
#         curr=curr.next
#         clone_curr=clone_curr.next

#     return clone_head

# values=[7,2,6,4,1,3,9]
# random_indicies=[None,1,0,2,4,6,5]
# Original=Creating_Linked_List(values,random_indicies)
# Display_Linked_List(Original)

# Copied_clone=Copy_random_list(Original)
# Display_Linked_List(Copied_clone)


# Add two numbers
# optimal solution
# time complexity=O(max(n,m))
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# def Create_Linked_List(arr):
#     if not arr:
#         return None
    
#     head=Node(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(val)
#         curr=curr.next

#     return head

# def Add_two_numbers(l1,l2):
#     dummy=Node(0)
#     curr=dummy
#     carry=0

#     while l1 or l2 or carry:
#         l1_val=l1.val if l1 else 0
#         l2_val=l2.val if l2 else 0

#         total=l1_val+l2_val+carry
#         carry=total//10
#         new_val=total%10

#         curr.next=Node(new_val)
#         curr=curr.next

#         if l1:
#             l1=l1.next 
#         if l2:
#             l2=l2.next

#     return dummy.next

# def Display_Linked_List(head):
    
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")


# l1=Create_Linked_List([2,4,3])
# l2=Create_Linked_List([5,6,4])
# Display_Linked_List(l1)
# Display_Linked_List(l2)

# result=Add_two_numbers(l1,l2)
# Display_Linked_List(result)

# l1=Create_Linked_List([9,9,9,9])
# l2=Create_Linked_List([9,9])
# Display_Linked_List(l1)
# Display_Linked_List(l2)
# result=Add_two_numbers(l1,l2)
# Display_Linked_List(result)


# Find the duplicate number
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):

#         self.val=val
#         self.next=next

# def Create_Linked_List(arr):
#     head=Node(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(val)
#         curr=curr.next
#     return head

# def Display_Linked_List(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")

# def Find_Duplicate(nums):
#     slow=nums[0]
#     fast=nums[0]

#     while True:
#         slow=nums[slow]
#         fast=nums[nums[fast]]

#         if slow==fast:
#             break
    

#     slow=nums[0]
#     while slow!=fast:
#         slow=nums[slow]
#         fast=nums[fast]
#     return slow

# nums=[1,2,3,7,4,5,8,6,6,6]
# ll=Create_Linked_List(nums)
# Display_Linked_List(ll)
# print(nums)
# duplicate=Find_Duplicate(nums)
# print(duplicate)
# # n+1 input dena hai (if n=4 means=1,2,3,4(n) and 1 and more for duplicate(2,2))

# LRU Cache
# optimal solution
# time complexity=O(1)
# space complexity=O(n)

# from collections import OrderedDict
# class LRUCache:
#     def __init__(self,capacity):
#         self.cache=OrderedDict()
#         self.capacity=capacity

#     def get(self,key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self,key,value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key]=value

#         if len(self.cache)>self.capacity:
#             self.cache.popitem(last=False)

# Cache=LRUCache(3)
# Cache.put(1,10)
# Cache.put(2,20)
# print(Cache.get(1))
# Cache.put(3,30)
# Cache.put(1,100)
# Cache.put(2,200)
# print(Cache.get(1))
# print(Cache.get(2))
# Cache.put(4,40)
# Cache.put(5,50)
# print(Cache.get(7))

# Merge K lists 
# optimal solution
# Time complexity: O(nlogk)
# space complexity:O(k)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next

# class Solution:
#     def mergeKlists(self,lists):
#         if not lists or len(lists)==0:
#             return None

#         while len(lists)>1:
#             merge_lists=[]
#             for i in range(0,len(lists),2):
#                 l1=lists[i]
#                 l2=lists[i+1] if (i+1) < len(lists) else None
#                 merge_lists.append(self.merge2lists(l1,l2))
#             lists=merge_lists
#         return lists[0]

#     def merge2lists(self,l1,l2):
#         dummy=Node(0)
#         curr=dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next=l1
#                 l1=l1.next
#             else:
#                 curr.next=l2
#                 l2=l2.next
#             curr=curr.next

#         curr.next=l1 if l1 else l2
#         return dummy.next

# def Create_Linked_List(arr):
#     head=Node(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(val)
#         curr=curr.next
#     return head

# def Display_Linked_List(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")

# l1=Create_Linked_List([1,2,4,6])
# l2=Create_Linked_List([3,4,7,9])
# l3=Create_Linked_List([6,7,8,9])
# l4=Create_Linked_List([2,3,7,8])

# sol=Solution()
# result=sol.mergeKlists([l1,l2,l3,l4])
# Display_Linked_List(result)

# Reverse Nodes In K Group
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# class Node:
#     def __init__(self,val=0,next=None):
#         self.val=val
#         self.next=next
# class Solution:
    
#     def reverseKgroups(self,head,k):
#         dummy=Node(0,head)
#         groupPrev=dummy

#         while True:
#             kth=self.getknodes(groupPrev,k)
#             if not kth:
#                 break
#             groupNext=kth.next

#             prev=kth.next
#             curr=groupPrev.next

#             while curr!=groupNext:
#                 temp=curr.next
#                 curr.next=prev
#                 prev=curr
#                 curr=temp

#             temp=groupPrev.next
#             groupPrev.next=kth
#             groupPrev=temp

#         return dummy.next

#     def getknodes(self,curr,k):
#         while curr and k>0:
#             curr=curr.next
#             k-=1
#         return curr

# def Create_Linked_List(arr):
#     if not arr:
#         return None

#     head=Node(arr[0])
#     curr=head
#     for val in arr[1:]:
#         curr.next=Node(val)
#         curr=curr.next
#     return head

# def Display_Linked_List(head):
#     curr=head
#     while curr:
#         print(curr.val,end="->")
#         curr=curr.next
#     print("None")

# arr=[int(x) for x in input().split()]
# ll=Create_Linked_List(arr)
# k=int(input())
# Display_Linked_List(ll)
# Sol=Solution()
# result=Sol.reverseKgroups(ll,k)
# Display_Linked_List(result)





