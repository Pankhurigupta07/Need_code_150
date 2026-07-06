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
# brute force
# time complexity=O(NlogN)
# space complexity=O(N)


def check_anagram(w1,w2):
    if len(w1)!=len(w2):
        return False

    return "".join(sorted(w1))=="".join(sorted(w2))

word1=input()
word2=input()
print(check_anagram(word1,word2))

