import sys

input = sys.stdin.readline


# x가 속한 그래프의 루트 노드(대표값)을 반환
def find(x: int) -> int:
    # x의 루트 노드가 자기 자신인 경우, 연결된 노드가 없는 경우
    # 자기 자신을 참조하는 노드가 루트 노드다.
    if parent[x] != x:
        parent[x] = find(parent[x])  # 재귀 중에 최적화 수행
    return parent[x]


# x와 y가 속한 두 그래프를 하나로 합집합 연산을 수행
def union(x: int, y: int) -> None:
    a = find(x)
    b = find(y)

    # x와 y가 동일한 속한 그래프가 동일하다면 합집합 연산을 수행 하지 않음
    if a == b:
        return

    # x 와 y 중에 크기가 더 큰 그래프에 작은 그래프를 합침
    if graph_sizes[a] > graph_sizes[b]:
        parent[b] = a
        graph_sizes[a] += graph_sizes[b]
    else:
        parent[a] = b
        graph_sizes[b] += graph_sizes[a]


T = int(input())
for _ in range(T):
    F = int(input())
    name_info = {}
    cur_Num = 0
    parent = []
    graph_sizes = []

    for i in range(F):
        x, y = input().split()

        # 초기화
        # 자기 자신을 참조하는 그래프 하나 생성
        if x not in name_info:  # name_info에 없으면 값을 저장
            name_info[x] = cur_Num
            parent.append(cur_Num)  # x노드의 부모 노드를 저장함
            graph_sizes.append(1)  # x노드가 속한 그래프의 크기를 저장하는 배열
            cur_Num += 1

        if y not in name_info:
            name_info[y] = cur_Num
            parent.append(cur_Num)
            graph_sizes.append(1)
            cur_Num += 1

        union(name_info[x], name_info[y])

        print(graph_sizes[find(name_info[x])])
