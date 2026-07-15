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

def longest_substring_without_repeating_characters(word):

    mp={}
    l=0
    res=0

    for r in range(len(word)):
        if word[r] in mp:
            l=max(mp[word[r]]+1,l)
        mp[word[r]]=r
        res=max(res,r-l+1)

    return res

word=input()
print(longest_substring_without_repeating_characters(word))












