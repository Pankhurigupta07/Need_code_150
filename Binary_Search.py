#Binary Search
#optimal solution
#Time complexity=O(logn)
# space complexity=O(1)

# def Binary_Search(arr,target):
    
#     start=0
#     end=len(arr)-1

#     while start<=end:
#         mid=(start+end)//2 
#         if arr[mid]==target:
#             return mid

#         elif arr[mid]<target:
#             start=mid+1

#         else:
#             end=mid-1

#     return -1

# arr=[int(x) for x in input().split()]
# target=int(input())
# print(Binary_Search(arr,target))