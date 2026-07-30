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

# Search a 2D matrix
# Better approach
# Time complexity=O(mlog(n))
# Space complexity=(1)

# def Search_in_2D_matrix(matrix,target):
#     for i in range(len(matrix)):
#         start=0
#         end=len(matrix[0])-1
    
#         if matrix[i][0]<=target<=matrix[i][-1]:
#             while start<=end:
#                 mid=(start+end)//2
#                 if matrix[i][mid]==target:
#                     return True

#                 elif matrix[i][mid]<target:
#                     start=mid+1
            
#                 else:
#                     end=mid-1

#     return False

# rows=int(input("Entre the no.of rows: "))
# matrix=[]
# for r in range(rows):
#     row=list(map(int,input().split()))
#     matrix.append(row)
# target=int(input())
# print(Search_in_2D_matrix(matrix,target))