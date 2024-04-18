import sys

input = sys.stdin.readline


def run_test_case(test_input):
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)
        if a == b:
            return

        if friendCount[a] > friendCount[b]:
            parent[b] = a
            friendCount[a] += friendCount[b]
        else:
            parent[a] = b
            friendCount[b] += friendCount[a]

    def input():
        return test_input.pop(0)

    T = int(input())
    for _ in range(T):
        F = int(input())
        nameInfo = {}
        curNum = 0
        parent = []
        friendCount = []

        for i in range(F):
            x, y = input().split()

            if x not in nameInfo:
                nameInfo[x] = curNum
                parent.append(curNum)
                friendCount.append(1)
                curNum += 1

            if y not in nameInfo:
                nameInfo[y] = curNum
                parent.append(curNum)
                friendCount.append(1)
                curNum += 1

            union(nameInfo[x], nameInfo[y])

            print(friendCount[find(nameInfo[x])])


test_input = [
    "1",
    "4",
    "Fred Barney",
    "Barney Betty",
    "Betty Wilma",
    "Barney Wilma"
]

# 테스트 케이스 실행
run_test_case(test_input)
