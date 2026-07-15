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
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# def two_sum(arr,target):
#     n=len(arr)
#     start=0
#     end=n-1
    
#     while start<end:
#         if arr[start]+arr[end]==target:
#             return[start,end]
#         elif arr[start]+arr[end]<target:
#             start+=1
#         else:
#             end-=1
#     return []

# arr=[int(x) for x in input().split()]
# target=int(input())
# print(two_sum(arr,target))


# Three sum
# optimal approach
# time complexity=O(n²)
# space complexity=O(1)

# def three_sum(arr):
#     n=len(arr)
#     result=[]
#     arr.sort()

#     for i in range(n):

#         if i>0 and arr[i]==arr[i-1]:
#             continue

#         start=i+1
#         end=n-1

#         while start<end:
#             current_sum=arr[i]+arr[start]+arr[end]
#             if current_sum==0:
#                 result.append([arr[i],arr[start],arr[end]])

#                 start+=1
#                 end-=1

#                 while start<end  and arr[start]==arr[start-1]:
#                     start+=1
#                 while start<end  and arr[end]==arr[end+1]:
#                     end-=1
                
#             elif current_sum<0:
#                 start+=1
#             else:
#                 end-=1

#     return result

# arr=[int(x) for x in input().split()]
# print(three_sum(arr))

# optimal solution
# Container with the most water
# time complexity=O(n)
# space complexity=O(1)

# def Container_with_the_most_water(arr):
#     n=len(arr)
#     start=0
#     end=n-1
#     vol=0

#     while start<end:
#         width=end-start
#         if(arr[start]<arr[end]):
#             current_vol=arr[start]*width
#             vol=max(vol,current_vol)
#             start+=1

#         else:
#             current_vol=arr[end]*width
#             vol=max(vol,current_vol)
#             end-=1

#     return vol

# arr=[int(x) for x in input().split()]
# print(Container_with_the_most_water(arr))

# Trapping rain water
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# def Trapping_rain_water(height):

#     if not height or len(height)<3:
#         return 0

#     n=len(height)
#     left=0
#     right=n-1
#     left_max=0
#     right_max=0
#     total_water=0

#     while left<right:
#         if height[left]<=height[right]:
#             if height[left]>=left_max:
#                 left_max=height[left]

#             else:
#                 total_water+= left_max-height[left]

#             left+=1

#         else:
#             if height[right]>=right_max:
#                 right_max=height[right]

#             else:
#                 total_water+= right_max-height[right]

#             right-=1

#     return total_water

# arr=[int(x) for x in input().split()]
# print(Trapping_rain_water(arr))

# longest substring without repeating characters
# brute force
# time complexity=O(n²)
# space comlplexity=O(n)

