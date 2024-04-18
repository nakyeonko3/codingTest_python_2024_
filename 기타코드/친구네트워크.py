def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[a] = b
        friendCount[b] += friendCount[a]


T = int(input())
for _ in range(T):
    F = int(input())
    nameInfo = {}
    curNum = 0
    parent = []
    friendCount = []

    for i in range(F):
        x, y = input().split()

        if x not in nameInfo:  # dictionary에 없으면
            nameInfo[x] = curNum  # dictionary에 추가
            parent.append(curNum)  # 부모목록에도 추가
            friendCount.append(1)  # 친구 숫자 새는곳에도 추가.
            curNum += 1

        if y not in nameInfo:
            nameInfo[y] = curNum
            parent.append(curNum)
            friendCount.append(1)
            curNum += 1

        union(nameInfo[x], nameInfo[y])

        print(friendCount[find(nameInfo[x])])