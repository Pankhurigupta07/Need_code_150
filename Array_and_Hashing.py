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


# valid anagram
# better approch
# time complexity=O(NlogN)
# space complexity=O(N)

# def check_anagram(w1,w2):
#     if len(w1)!=len(w2):
#         return False

#     return "".join(sorted(w1))=="".join(sorted(w2))

# word1=input()
# word2=input()
# print(check_anagram(word1,word2))

# optimal approch
# time complexit=O(n)
# space complexity=O(1)
# using hash map

# from collections import Counter

# def check_anagram(w1,w2):
#     if (Counter(w1)==Counter(w2)):
#         return True
#     return False

# word1=input()
# word2=input()
# print(check_anagram(word1,word2))

# brute force
# def check_anagram(w1,w2):
#     if(len(w1)!=len(w2)):
#         return False

#     word2=list(w2)

#     for i in w1:
#         if i in word2:
#             word2.remove(i)
#         else:
#             return False

#     return True
        
# word1=input()
# word2=input()
# print(check_anagram(word1,word2))

#time complexity=O(n²)
#space complexity=O(n)


# two sum 
# brute force
# time complexity=O(n²)
# space complexity=O(1)
# def two_sum(l,t_num,n):
#     for i in range(n):
#         for j in range(1,n):
#             if(l[i]+l[j]==t_num):
#                 index=i,j
#     return index

# num_list=list(map(int,input().split()))
# target_num=int(input())
# print(two_sum(num_list,target_num,len(num_list)))


# optimal approach 
# time complexity=O(n)
# space complexity=O(1)

# def two_sum(arr,t_num,n):
#     start=0
#     for i in range(1,n):
#         if(arr[start]+arr[i]==t_num):
#             return start,i
#         start+=1

# num_list=list(map(int,input().split()))
# target_num=int(input())
# print(two_sum(num_list,target_num,len(num_list)))


# group anagram
# def group_anagram(arr):
#     anagram_map={}

#     for word in arr:
#         sorted_word="".join(sorted(word))

#         if sorted_word not in anagram_map:
#             anagram_map[sorted_word]=[]

#         anagram_map[sorted_word].append(word)

#     return list(anagram_map.values())

# arr=[ x for x in input().split()]
# print(group_anagram(arr))

# #time complexity=O(n.klogk)
# #space complexity=O(n.k)


#top k frequent elements
#better approch
# from collections import Counter
# def top_k_frequent_elements(arr,k):

#     frequency=Counter(arr)
#     sorted_frequency=frequency.most_common(k)
#     return[item[0] for item in sorted_frequency]
    
# arr=list(map(int,input().split()))
# k=int(input())
# print(top_k_frequent_elements(arr,k))

#Time Complexity: O(NlogK)
# space complexity:O(N)

# optimal approach

# from collections import Counter
# def top_k_frequent_elements(arr,k):

#     count=Counter(arr)

#     bucket=[ [] for _ in range(len(arr)+1)]

#     for num, freq in count.items():
#         bucket[freq].append(num)
        
#     result=[]
#     for i in range(len(bucket)-1,0,-1):
#         for num in bucket[i]:
#             result.append(num)
#             if len(result)==k:
#                 return result

# arr=list(map(int,input().split()))
# k=int(input())
# print(top_k_frequent_elements(arr,k))

# time complexity=O(N)
# space complexity=O(N)


# Encode and Decode string

# def encode(strs):
#     result=""
#     for s in strs:
#         result+= str(len(s))+ "#" +s
#     return result

# def decode(s):
#     res=[]
#     i=0
#     while i < len(s):
#         j=i
#         while s[j]!="#":
#             j+=1

#         length=int(s[i:j])

#         word=s[j+1:j+1+length]
#         res.append(word)

#         i=j+1+length

#     return res

# arr=input().split()
# s=encode(arr)
# print(s)
# print(decode(s))

# time complexity=O(N)
# space complexity=O(1)

#product of array except self

# def product_of_array_except_self(arr,n):
# brute force
    
#     l=[]
    
#     for i in range(n):
#         product=1
#         for j in arr:
#             product=product*j

#         a=product//arr[i]
#         l.append(a)
        
#     return l

# arr=[int(x) for x in input().split()]
# print(product_of_array_except_self(arr,len(arr)))

# time complexity=O(n²)
# space complexity=O(n)

# brute force approach
#time complexity=O(n²)
#space complexity=O(n)

# import math
# def product_of_array_except_self(arr,n):
#     l=[]
#     for i in range(n):
#         left_prod=math.prod(arr[:i])
#         right_prod=math.prod(arr[i+1:])
#         a=left_prod*right_prod
#         l.append(a)

#     return l

# arr=[int(x) for x in input().split()]
# print(product_of_array_except_self(arr,len(arr)))



# optimal approach

# def product_of_array_except_self(arr):
#     n=len(arr)
#     result=[1]*n

#     left_prod=1
#     for i in range(n):
#         result[i]=left_prod
#         left_prod*=arr[i]

#     right_prod=1
#     for i in range(n-1,-1,-1):
#         result[i]*=right_prod
#         right_prod*=arr[i]

#     return result

# arr=[int(x) for x in input().split()]
# print(product_of_array_except_self(arr))

# Time complexity=O(N)
# Space complexity=O(1)


# valid sudoku
# def is_valid_sudoku(board):
#     rows=[0]*9
#     cols=[0]*9
#     squares=[0]*9

#     for r in range(9):
#         for c in range(9):
#             if(board[r][c]=="."):
#                 continue

#             val=int(board[r][c])-1
#             if(1 << val) & rows[r]:
#                 return False

#             if(1 << val) & cols[r]:
#                 return False

#             if(1 << val) & squares[ (r//3) * 3 + (c//3) ]:
#                 return False

#             rows[r] |= (1 << val)
#             cols[c] |= (1 << val)
#             squares[ (r//3) * 3 + (c//3) ] |= (1 << val)

#     return True

# user_board=[input().split() for _ in range(9)]

# if(is_valid_sudoku(user_board)):
#     print("Valid")

# else:
#     print("Invalid")

# Time complexity=O(N²)
# Space complexity=O(N)


# longest consecutive sequence
# brute force 
# time complexity=O(NlogN)
# space complexity=O(N)

# def longest_consecutive_sequence(arr):

#     if not arr:
#         return []

#     arr.sort()

#     longest=[]
#     current_sub_long=[arr[0]]
#     n=len(arr)
#     for i in range(1,n):
#         if (arr[i]==arr[i-1]+1):
#             current_sub_long.append(arr[i])
        
#         elif(arr[i]==arr[i-1]):
#             continue

#         else:
#             longest.append(current_sub_long)

#             current_sub_long=[arr[i]]

#     longest.append(current_sub_long)

#     longest_list=max(longest,key=len)
#     return longest_list

# arr=[int(x) for x in input().split()]
# print(longest_consecutive_sequence(arr))


# longest consecutive sequence
# optimal solution
# time complexity=O(n)
# space complexity=O(n)

# def longest_consecutive_sequence(arr):

#     num_set=set(arr)
#     longest_streak=0

#     for num in num_set:

#         if num-1 not in num_set:

#             current_num=num
#             current_streak=1

#             while current_num+1 in num_set:
                
#                 current_num+=1
#                 current_streak+=1
            
#             longest_streak=max(longest_streak,current_streak)

#     return longest_streak

# arr=[int(x) for x in input().split()]
# print(longest_consecutive_sequence(arr))






            
