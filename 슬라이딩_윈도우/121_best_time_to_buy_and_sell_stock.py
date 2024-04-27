prices = [7, 1, 5, 3, 6, 4]

combinations_list_1 = []
max_profit = 0
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        profit = prices[j] - prices[i]
        if max_profit < profit:
            max_profit = profit

print(max_profit)


# # itertools 모듈의 combinations 함수 이용
# # itertools.combinations 함수에 매개변수로 리스트와 조합의 길이를 넣어주면
# # 해당 리스트의 조헙의 개수를 알아낼 수 있다
# from itertools import combinations
#
# combinations_list = list(combinations(prices, 2))
# print(combinations_list)
