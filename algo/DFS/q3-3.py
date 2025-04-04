"""
정점의 개수 n, 간선의 개수 m

m개의 간선 정보가 주어졌을 때,
연결 요소의 개수를 구하시오


연결 요소란?

DFS로 연결 가능한 노드들의 집합

예: 1 - 2 - 3, 4 - 5, 6 → 총 3개의 연결 요소
"""
n = 6
edges = [(1, 2), (2, 5), (3, 4), (5, 4)]

출력: 3

x = len(edges)
y = len(edges[0])

visited = [False] * (n + 1)

count = 0

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결


def dfs(x):
    visited[x] = True
    for q in graph[x]:
        print(q)  # 2 -> (1 - 5) -> (2 - 4) -> 3 -> 4
        if not visited[q]:
            print(visited[q])  # False -> False -> False
            dfs(q)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1


print(count)
