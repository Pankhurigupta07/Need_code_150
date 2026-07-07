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


# top k frequent elements
# better approch
# from collections import Counter
# def top_k_frequent_elements(arr,k):

#     frequency=Counter(arr)
#     sorted_frequency=(frequency.most_common(k))
#     return[item[0] for item in sorted_frequency]
    
# arr=list(map(int,input().split()))
# k=int(input())
# print(top_k_frequent_elements(arr,k))

#Time Complexity: O(NlogK)
# space complexity:O(N)