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


def valid_palindrome(word):

    n=len(word)
    left=0
    right=n-1

    while left<right:
        if word[left]!=word[right]:
            return False
        left+=1
        right-=1
    return True

word=input()
if(valid_palindrome(word)):
    print("Valid")

else:
    print("Invalid")

