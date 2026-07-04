# brute force
#Contains Duplicates
# def contain_duplicate(arr,n):
#     for i in range(n):
#         for j in range(i+1,n):
#             if(arr[i]==arr[j]):
#                 return True

#     return False

# arr=[int(x) for x in input().split()]

# print(contain_duplicate(arr,len(arr)))
#tc->0(n²)


#optimal approch
# def contain_duplicate(arr,n):
#     set1=set()
#     for i in range(n):
#         if(arr[i] in set1):
#             return True
#         else:
#             set1.add(arr[i])
#     return False

# arr=[int(x) for x in input().split()]
# print(contain_duplicate(arr,len(arr)))
#tc->O(n)