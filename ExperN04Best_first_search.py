import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

h = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 4
}

start = 'A'
goal = 'E'

queue = [(h[start], start)]
visited = set()

while queue:
    value, node = heapq.heappop(queue)

    if node in visited:
        continue

    print(node)
    visited.add(node)

    if node == goal:
        print("Goal found")
        break

    for neighbour in graph[node]:
        heapq.heappush(queue, (h[neighbour], neighbour))