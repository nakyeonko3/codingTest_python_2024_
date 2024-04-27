elements = [1, 2, 3, 4, 5]


# 그리고 파이썬은 rang(10)을 설정하면 0~9까지 나온다
# range(1,10)이면 1에서 까지 생성된다. 두번째 숫자애서 1을 밴 값까지만 생성된다는 뜻이다


# 리스트에서 for 반복문을 이용해서 2개의 원소를 선택하는 모든 조합만들기

# 이중 반복문
# 두 번째 반복문의 시작 지점을 첫 번째 반복문의 시점보다 하나 더 크게 설정해주면 중복을 피할 수 있다.

combinations_list_1 = []
for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        combinations_list_1.append((elements[i], elements[j]))

print(combinations_list_1)


# itertools 모듈의 combinations 함수 이용
# itertools.combinations 함수에 매개변수로 리스트와 조합의 길이를 넣어주면
# 해당 리스트의 조헙의 개수를 알아낼 수 있다
from itertools import combinations

combinations_list = list(combinations(elements, 2))
print(combinations_list)
