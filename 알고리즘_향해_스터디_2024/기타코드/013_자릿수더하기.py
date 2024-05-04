# 자연수 n개가 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return하도록 solution 함수를 완성해주세요.
def solution(n: int) -> int:
    min_number = n - 1
    for i in range(1, n):
        # print(i)
        if n % i == 1:
            # print(i)
            if i < min_number:
                min_number = i
                # print(i)
    return min_number


if __name__ == '__main__':
    print(solution(42))
