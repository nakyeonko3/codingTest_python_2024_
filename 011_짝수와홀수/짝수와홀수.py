def solution(num: int):
    if num % 2 == 0:
        return "Odd"
    elif num % 2 == 1:
        return "Even"
    else:
        return None

if __name__ == '__main__':
    print(solution(1))
    print(solution(2))
#
# if __name__ == "__main__":
#     print(solution(2))
