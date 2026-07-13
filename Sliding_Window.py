# Best time to buy and sell
# optimal solution
# time complexity=O(n)
# space complexity=
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