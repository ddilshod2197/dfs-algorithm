class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def dfs(self, start_vertex):
        visited = [False] * self.vertices
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._dfs_helper(neighbor, visited)


# Misol uchun graf yaratish
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

# DFS boshlash uchun boshlang'ich nuqta tanlash
graph.dfs(0)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Grafni yaratish uchun `Graph` klassidan ob'ekt yaratish.
2. Grafga qo'shni uchun `add_edge` metodi orqali qo'shni qo'shish.
3. DFS boshlash uchun boshlang'ich nuqta tanlash.
4. `dfs` metodi orqali DFS boshlash.
