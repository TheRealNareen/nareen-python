n = int(input("Enter the number of users: "))

graph = {i: [] for i in range(n)}

connections = int(input("Enter the number of friendships: "))

print("Enter friendships:")
for _ in range(connections):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

while True:
    print("\n===== SOCIAL NETWORK =====")
    print("1. Display Friends")
    print("2. BFS Traversal")
    print("3. DFS Traversal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user = int(input("Enter user: "))

        if user in graph:
            print("Friends of User", user, ":", graph[user])
        else:
            print("Invalid user.")

    elif choice == 2:
        start = int(input("Enter starting user: "))

        if start not in graph:
            print("Invalid user.")
            continue

        visited = set()
        queue = [start]
        visited.add(start)
        bfs = []

        while queue:
            user = queue.pop(0)
            bfs.append(user)

            for friend in graph[user]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)

        print("BFS Traversal:", bfs)

    elif choice == 3:
        start = int(input("Enter starting user: "))

        if start not in graph:
            print("Invalid user.")
            continue

        visited = set()
        dfs = []

        def dfs_traversal(user):
            visited.add(user)
            dfs.append(user)

            for friend in graph[user]:
                if friend not in visited:
                    dfs_traversal(friend)

        dfs_traversal(start)

        print("DFS Traversal:", dfs)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
