n = int(input("Enter the total number of users: "))

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
adj_list = {i: [] for i in range(n)}

while True:
    print("1. Add Friendship")
    print("2. Display Adjacency Matrix")
    print("3. Display Adjacency List")
    print("4. Check Friendship")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        u, v = map(int, input("Enter two users: ").split())

        if 0 <= u < n and 0 <= v < n:
            if adj_matrix[u][v] == 0:
                adj_matrix[u][v] = 1
                adj_matrix[v][u] = 1
                adj_list[u].append(v)
                adj_list[v].append(u)
                print("Friendship added successfully.")
            else:
                print("They are already friends.")
        else:
            print("Invalid user number.")

    elif choice == 2:
        print("\n- Adjacency Matrix -")
        print("   ", end="")
        for i in range(n):
            print(i, end=" ")
        print()

        for i in range(n):
            print(i, " ", end="")
            for j in range(n):
                print(adj_matrix[i][j], end=" ")
            print()

    elif choice == 3:
        print("\n- Adjacency List -")
        for user in range(n):
            print(f"User {user} -> ", end="")
            if adj_list[user]:
                print(*adj_list[user], sep=" -> ")
            else:
                print("No friends")

    elif choice == 4:
        u, v = map(int, input("Enter two users to check friendship: ").split())

        if 0 <= u < n and 0 <= v < n:
            if adj_matrix[u][v] == 1:
                print(f"Matrix: User {u} and User {v} are friends.")
            else:
                print(f"Matrix: User {u} and User {v} are not friends.")

            if v in adj_list[u]:
                print(f"List: User {u} and User {v} are friends.")
            else:
                print(f"List: User {u} and User {v} are not friends.")
        else:
            print("Invalid user number.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
