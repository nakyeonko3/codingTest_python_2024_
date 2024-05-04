import sys

input = sys.stdin.readline
[n, m] = [int(b) for b in input().split()]
lectures = [int(a) for a in input().split()]

start = max(lectures)  # 최소 블루레이 크기의 하한
end = sum(lectures)  # 최소 블루레이 크기의 상한


def get_cnt(size: int, lectures: list):
    cnt = 1  # 블루레이 개수
    total = 0  # 현재 블루레이에 녹화된 강의 길이 합
    for lecture in lectures:
        if total + lecture > size:
            cnt += 1
            total = lecture
        else:
            total += lecture
    return cnt


def get_min_blurary_size(start: int, end: int, lectures: list):
    while start <= end:
        mid = (start + end) // 2
        if get_cnt(mid, lectures) <= m:
            end = mid - 1
        else:
            start = mid + 1
    return start


result = get_min_blurary_size(start, end, lectures)
print(result)

# if __name__ == '__main__':
#     get_min_blurary_size(start, end, lectures)