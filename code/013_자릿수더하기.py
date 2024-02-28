def solution(n):
    n = [*str(n)]
    return sum([int(x) for x in n])


if __name__ == '__main__':
    print(solution(1342))
