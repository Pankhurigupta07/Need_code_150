# Best time to buy and sell
# optimal solution
# time complexity=O(n)
# space complexity=O(1)
# def buy_and_sell(arr):
#     n=len(arr)
#     buy=0
#     max_profit=0

#     for sell in range(1,n):
#         if arr[sell]>arr[buy]:
#             current_profit=arr[sell]-arr[buy]
#             max_profit=max(max_profit,current_profit)

#         else:
#             buy=sell

#     return max_profit

# arr=[int(x) for x in input().split()]
# print(buy_and_sell(arr))



# def longest_substring_without_repeating_characters(word):

#     start=0
#     nextt=0
#     new_word=""
#     max_len=0

#     while nextt<len(word):

#         if word[nextt] not in new_word:
#             new_word+=word[nextt]
#             nextt+=1
#             max_len=max(max_len,len(new_word))

#         else:
#             start+=1
#             new_word=word[start:nextt]
            
#     return max_len
        
# word=input()
# print(longest_substring_without_repeating_characters(word))



# optimal approach
# time complexity=O(n)
# space complexity=O(m)

# def longest_substring_without_repeating_characters(word):

#     mp={}
#     l=0
#     res=0

#     for r in range(len(word)):
#         if word[r] in mp:
#             l=max(mp[word[r]]+1,l)
#         mp[word[r]]=r
#         res=max(res,r-l+1)

#     return res

# word=input()
# print(longest_substring_without_repeating_characters(word))

# longest repeating character replacement
# optimal approach
# time complexity=O(n)
# space complexity=O(1)

# def longest_repeating_character_replacement(word,k):
#     max_count={}
#     left=0
#     max_frequency=0
#     max_lenght=0

#     for right in range(len(word)):
#         max_count[word[right]]= max_count.get(word[right],0)+1
#         # if word[right] in max_count:
#             #max_count[word[right]]+=1
#         #else:
#             #max_count[word[right]]=1
#         max_frequency=max(max_frequency,max_count[word[right]])

#         if(right-left+1)-max_frequency>k:
#             max_count[word[left]]-=1
#             left+=1
#         max_lenght=max(max_lenght,right-left+1)
    
#     return max_lenght

# word=input()
# k=int(input())
# print(longest_repeating_character_replacement(word,k))

#  permutation_in_string
# optimal solution
# time complexity=O(n)
# space complexity=O(1)

# def permutation_in_string(word1,word2):

#     if len(word1)> len(word2):
#         return False

#     word1_mp={}
    
#     for s in range(len(word1)):
#         if word1[s] in word1_mp:
#             word1_mp[word1[s]]+=1
#         else:
#             word1_mp[word1[s]]=1

#     word2_mp={}
#     match=0
#     left=0
#     required=len(word1_mp)
#     for right in range(len(word2)):
#         char_in=word2[right]

#         if char_in in word1_mp:
#             word2_mp[char_in]=word2_mp.get(char_in,0)+1
#             if word1_mp[char_in]==word2_mp[char_in]:
#                 match+=1

#         if right-left+1>len(word1):
#             char_out=word2[left]

#             if char_out in word1_mp:
#                 if word2_mp[char_out]==word1_mp[char_out]:
#                     match-=1
#                 word2_mp[char_out]-=1
#             left+=1

#         if match==required:
#             return True

#     return False

# word1=input()
# word2=input()
# print(permutation_in_string(word1,word2))


# Minimum Window Substring
# optimal solution
# time complexity=O(M+N)
# space complexity=O(1)

# def Minimum_Window_Substring(s,t):

#     if len(s)<len(t):
#         return""

#     t_count={}
#     for char in t:
#         t_count[char]=t_count.get(char,0)+1

#     required=len(t_count)
#     match=0
#     count_window={}
#     left=0
#     min_len=float('inf')
#     start_idx=0

#     for right in range(len(s)):
#         char_in=s[right]
#         if char_in in t_count:
#             count_window[char_in]=count_window.get(char_in,0)+1
#             if count_window[char_in]==t_count[char_in]:
#                 match+=1

#         while(required==match):
#             current_len=right-left+1
#             if current_len<min_len:
#                 min_len=current_len
#                 start_idx=left

#             char_out=s[left]

#             if char_out in t_count:
#                 if t_count[char_out]==count_window[char_out]:
#                     match-=1
#                 count_window[char_out]-=1

#             left+=1

#     if min_len==float('inf'):
#         return""
#     else:
#         return s[start_idx : start_idx + min_len] 

# s=input()
# t=input()
# print(Minimum_Window_Substring(s,t))





