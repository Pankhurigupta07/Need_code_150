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

def longest_repeating_character_replacement(word,k):
    max_count={}
    left=0
    max_frequency=0
    max_lenght=0

    for right in range(len(word)):
        max_count[word[right]]= max_count.get(word[right],0)+1
        # if word[right] in max_count:
            #max_count[word[right]]+=1
        #else:
            #max_count[word[right]]=1
        max_frequency=max(max_frequency,max_count[word[right]])

        if(right-left+1)-max_frequency>k:
            max_count[word[left]]-=1
            left+=1
        max_lenght=max(max_lenght,right-left+1)
    
    return max_lenght

word=input()
k=int(input())
print(longest_repeating_character_replacement(word,k))










