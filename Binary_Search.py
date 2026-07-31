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

# optimal approach
# Time complexity=O(logm*n)
# Space complexity=O(1)

# def Search_in_2D_Matrix(Matrix,target):
#     rows=len(Matrix)
#     cols=len(Matrix[0])

#     start=0
#     end=(rows*cols)-1

#     while start<=end:
#         mid=(start+end)//2

#         row=mid//cols
#         col=mid % cols

#         if Matrix[row][col]==target:
#             return True

#         elif Matrix[row][col]<target:
#             start=mid+1

#         else:
#             end=mid-1

#     return False

# rows=int(input("Enter the no. of rows: "))
# Matrix=[]
# for r in range(rows):
#     row=list(map(int,input().split()))
#     Matrix.append(row)
# target=int(input())
# print(Search_in_2D_Matrix(Matrix,target))


# Koko Eating bananas
# optimal solution
# tc=O(n log m)
# sc=O(1)

# from math import ceil
# def MinEatingSpeed(piles,H):

#     low=1
#     high=max(piles)

#     while low<high:
#         mid=(low+high)//2

#         total_hours=0
#         for p in piles:
#             total_hours+=ceil(p/mid)

#         if total_hours<=H:
#             high=mid

#         else:
#             low=mid+1

#     return low

# piles=[int(x) for x in input().split()]
# H=int(input())
# print(MinEatingSpeed(piles,H))