import sys
input = sys.stdin.readline
n = int(input())
arr = [int(num) for num in input().split()]

dp = [1] * n

print(dp)
# for i in range(1, n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
