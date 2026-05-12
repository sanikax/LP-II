import heapq

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def hs(start):
    count = 0

    for i in range(3):
        for j in range(3):
            if start[i][j] != 0 and start[i][j] != goal[i][j]:
                count += 1

    return count


def find_zero(start):
    for i in range(3):
        for j in range(3):
            if start[i][j] == 0:
                return i, j


def to_tuple(current):
    return tuple(tuple(row) for row in current)


def a_star(start):

    pq = []

    g = 0
    h = hs(start)
    f = g + h

    heapq.heappush(pq, (f, g, start, []))

    visited = set()

    while pq:

        f, g, current, path = heapq.heappop(pq)

        if to_tuple(current) in visited:
            continue

        visited.add(to_tuple(current))

        if goal == current:
            return path + [current]

        x, y = find_zero(current)

        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:

                new_state = [row[:] for row in current]

                new_state[x][y], new_state[nx][ny] = (
                    new_state[nx][ny],
                    new_state[x][y]
                )

                if to_tuple(new_state) not in visited:

                    new_g = g + 1
                    new_h = hs(new_state)
                    new_f = new_g + new_h

                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state, path + [current])
                    )

    return None


def print_path(path):

    for step, state in enumerate(path):

        print("Step:", step)

        for row in state:
            print(row)

        print()


print("Enter the initial state:")

initial = []

for i in range(3):
    row = list(map(int, input().split()))
    initial.append(row)

solution = a_star(initial)

if solution:
    print("\nSolution Exists:")
    print_path(solution)

else:
    print("Solution Doesn't exist")