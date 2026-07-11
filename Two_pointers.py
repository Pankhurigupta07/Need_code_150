# without using two poniter
#optimal solution
#time complexity=O(n)
#space complexity=O(1)
# valid palindrome
# def valid_palindrome(word):

#     n=len(word)

#     for i in range ((n//2)):
#         if word[i]!=word[n-i-1]:
#             return False 

#     return True

# word=input()
# if(valid_palindrome(word)):
#     print("Valid")

# else:
#     print("Invalid")

# using two pointer
#optimal approach
#time complexity=O(n)
#space complexity=O(1)

# def valid_palindrome(word):

#     n=len(word)
#     left=0
#     right=n-1

#     while left<right:
#         if word[left]!=word[right]:
#             return False
#         left+=1
#         right-=1
#     return True

# word=input()
# if(valid_palindrome(word)):
#     print("Valid")

# else:
#     print("Invalid")

# two sum without two pointer
# optimal approach 
# time complexity=O(n)
# space complexity=O(1)

# def two_sum(arr,target):
#     n=len(arr)
#     start=0
#     for i in range(1,n):
#         if arr[i]+arr[start]==target:
#             return start,i
#         start+=1
#     return index

# arr=[int(x) for x in input().split()]
# target=int(input())
# print(two_sum(arr,target))

# two pointer
def two_sum(arr,target):
    n=len(arr)
    start=0
    end=n-1
    
    while start<end:
        if arr[start]+arr[end]==target:
            return[start,end]
        elif arr[start]+arr[end]<target:
            start+=1
        else:
            end-=1
    return []

arr=[int(x) for x in input().split()]
target=int(input())
print(two_sum(arr,target))


