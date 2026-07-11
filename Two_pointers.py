# without using two poniter
#optimal solution
#time complexity=O(n)
#space complexity=O(1)
# valid palindrome
def valid_palindrome(word):

    n=len(word)

    for i in range ((n//2)):
        if word[i]!=word[n-i-1]:
            return False 

    return True

word=input()
if(valid_palindrome(word)):
    print("Valid")

else:
    print("Invalid")