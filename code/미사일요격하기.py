def get_first(item):
    return item[0]


def solution(targets):
    targets.sort(key=get_first)

    count = 0
    last = -1

    for start, end in targets:
        if start >= last:
            count += 1
            last = end
        else:
            last = min(last, end)

    return count


targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]

print(solution(targets))  # 3
