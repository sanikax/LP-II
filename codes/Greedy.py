import sys

# -------- SELECTION SORT --------
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_i = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j

        # swap
        arr[i], arr[min_i] = arr[min_i], arr[i]

        print("Step", i + 1, ":", arr)

    return arr


# -------- PRIM'S ALGORITHM --------
def prim(graph, V, labels):
    selected = [False] * V
    selected[0] = True

    edges = 0
    total = 0

    print("\nMST Edges:")

    while edges < V - 1:
        min_cost = sys.maxsize
        a = b = -1

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < min_cost:
                            min_cost = graph[i][j]
                            a, b = i, j

        print(labels[a], "-", labels[b], ":", min_cost)

        total += min_cost
        selected[b] = True
        edges += 1

    print("Total MST Weight =", total)


# -------- MAIN PROGRAM --------
def main():

    # Selection Sort
    print("=== Selection Sort ===")
    arr = list(map(int, input("Enter numbers: ").split()))

    print("Original:", arr)
    print("Sorted:")
    selection_sort(arr)

    # Prim's Algorithm
    print("\n=== Prim's Algorithm ===")

    V = int(input("Number of vertices: "))
    labels = input("Vertex labels: ").split()

    print("Enter adjacency matrix:")
    graph = [list(map(int, input().split())) for _ in range(V)]

    prim(graph, V, labels)


# run program
main()