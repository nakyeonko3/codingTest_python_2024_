# https://school.programmers.co.kr/learn/courses/30/lessons/12944
def solution(arr: list) -> int:
    answer = sum(arr) / len(arr)
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3]))
