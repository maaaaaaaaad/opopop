import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, u = heapq.heappop(q)
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            if new_cost := dist[u] + w; new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(q, (new_cost, v))
    return dist

graph = [
    [(1, 2), (2, 5)],
    [(0, 2), (2, 4), (3, 6)],
    [(0, 5), (1, 4), (3, 2), (4, 3)],
    [(1, 6), (2, 2), (4, 7)],
    [(2, 3), (3, 7), (5, 1)],
    [(4, 1)],
]
start = 0
dist = dijkstra(graph, start)
for i, d in enumerate(dist):
    print(f"노드 {i}까지의 최단 거리: {d}")
