# Invert Binary Tree
# Optimal solution
# Time complexity=O(n)
# Space complexity=O(n)

# from collections import deque
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right

# class Solution:
#     def Invert_Tree(self,root):
        
#         if not root:
#             return None

#         root.left,root.right=root.right,root.left
#         self.Invert_Tree(root.left)
#         self.Invert_Tree(root.right)

#         return root

# def build_tree_from_user_input(user_input):
    
#     if not user_input:
#         return None

#     vals=[]
#     for x in user_input:
#         if x.lower() in ("null","none"):
#             vals.append(None)

#         else:
#             vals.append(int(x))

#     root=TreeNode(vals[0])
#     queue=deque([root])
#     i = 1

#     while queue and i<len(vals):
#         curr=queue.popleft()

#         if i<len(vals) and vals[i] is not None:
#             curr.left=TreeNode(vals[i])
#             queue.append(curr.left)
#         i += 1


#         if i<len(vals) and vals[i] is not None:
#             curr.right=TreeNode(vals[i])
#             queue.append(curr.right)
#         i += 1


#     return root

# def print_level_order(root):
#     if not root:
#         print([])
#         return

#     result=[]
#     queue=deque([root])

#     while queue:
#         curr=queue.popleft()
#         if curr:
#             result.append(curr.val)
#             queue.append(curr.left)
#             queue.append(curr.right)

#     while result and result[-1] is None:
#         result.pop()

#     print(result)

# user_input=input().split()
# root=build_tree_from_user_input(user_input)

# Sol=Solution()
# inverted_tree=Sol.Invert_Tree(root)

# print_level_order(inverted_tree)




