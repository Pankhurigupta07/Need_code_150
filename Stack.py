#Stack Question
# using push pop operation
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


# Min Stack 
# Optimal Solution
# Time complexity=O(1)
# Stack complexity=O(n)

# class MinStack:

#     def __init__(self):
#         self.main_stack=[]
#         self.min_stack=[]

#     def push(self, val):
#         self.main_stack.append(val)

#         if (len(self.min_stack)==0 or val<=self.min_stack[-1]):
#             self.min_stack.append(val)

#     def pop(self):
        
#         if self.main_stack[-1]==self.min_stack[-1]:
#             self.min_stack.pop()

#         self.main_stack.pop()

#     def top(self):
#         return self.main_stack[-1]

#     def GetMin(self):
#         return self.min_stack[-1]

# s=MinStack()
# s.push(2)
# s.push(6)
# s.push(9)
# s.pop()
# print(f"Min is: {s.GetMin()}")
# print(f"Top is: {s.top()}")
# s.push(1)
# print(f"Min is: {s.GetMin()}")


# Evaluate Self Polish Notation
# Optimal Solution
# Time complexity=O(n)
# Stack complexity=O(n)


class Solution:
    def __init__(self):
        self.stack=[]

    def evalRPN(self,tokens):
        for tkn in tokens:
            if tkn=="+":
                self.stack.append(self.stack.pop()+self.stack.pop())
            elif tkn=="-":
                a,b=self.stack.pop(),self.stack.pop()
                self.stack.append(b-a)
            elif tkn=="*":
                self.stack.append(self.stack.pop()*self.stack.pop())
            elif tkn=="/":
                a,b=self.stack.pop(),self.stack.pop()
                self.stack.append(int(b/a))
            else:
                self.stack.append(int(tkn))

        return self.stack.pop()

S=Solution()
tokens=input().split()
print(S.evalRPN(tokens))

