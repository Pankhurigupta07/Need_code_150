#Stack Question
# Valid Parentheses
# optimal solution
# time complexity=O(n)
# space complexity=O(n)

# def Valid_Parenthese(Parentheses):

#     if len(Parentheses)==0:
#         return "invalid"

#     stack=[]
#     mp={")":"(", "]":"[", "}":"{"}

#     for s in Parentheses:
#         if s in mp:
#             top_element=stack.pop()

#             if mp[s]!=top_element:
#                  return "invalid"

#         else:
#              stack.append(s)
        
#     if len(stack)==0:
#         return "valid"

#     else:
#         return "invalid"

# Parentheses=input()
# print(Valid_Parenthese(Parentheses))