import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.parent = None

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

start_x, start_y = 0, 0
end_x, end_y = 4, 4
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_valid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def heuristic(x, y):
    return abs(end_x - x) + abs(end_y - y)

def a_star():
    pq = []
    heapq.heappush(pq, Node(start_x, start_y))
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    while pq:
        current = heapq.heappop(pq)
        visited[current.x][current.y] = True

        if current.x == end_x and current.y == end_y:
            # Path found, reconstruct path
            path = []
            while current is not None:
                path.append((current.x, current.y))
                current = current.parent
            path.reverse()
            print("Path:", path)
            return

        for i in range(4):
            next_x = current.x + dx[i]
            next_y = current.y + dy[i]
            if is_valid(next_x, next_y) and grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                neighbor = Node(next_x, next_y)
                neighbor.g = current.g + 1
                neighbor.h = heuristic(next_x, next_y)
                neighbor.parent = current
                heapq.heappush(pq, neighbor)

    print("No path found!")

if __name__ == "__main__":
    a_star()
