class LogNode:
    def __init__(self, visitor_name, entry_time, purpose):
        self.visitor_name = visitor_name
        self.entry_time = entry_time
        self.purpose = purpose
        self.left = None
        self.right = None

    def get_details(self):
        return f"[Name: {self.visitor_name} | Time: {self.entry_time} | Purpose: {self.purpose}]"

class VisitorLogBook:
    def __init__(self):
        self.root = None

    def insert(self, visitor_name, entry_time, purpose):
        if self.root is None:
            self.root = LogNode(visitor_name, entry_time, purpose)
        else:
            self._insert_recursive(self.root, visitor_name, entry_time, purpose)

    def _insert_recursive(self, current_node, visitor_name, entry_time, purpose):
        if visitor_name.lower() < current_node.visitor_name.lower():
            if current_node.left is None:
                current_node.left = LogNode(visitor_name, entry_time, purpose)
            else:
                self._insert_recursive(current_node.left, visitor_name, entry_time, purpose)
        else:
            if current_node.right is None:
                current_node.right = LogNode(visitor_name, entry_time, purpose)
            else:
                self._insert_recursive(current_node.right, visitor_name, entry_time, purpose)

    def delete(self, visitor_name):
        self.root = self._delete_recursive(self.root, visitor_name)

    def _delete_recursive(self, node, visitor_name):
        if node is None:
            return node

        if visitor_name.lower() < node.visitor_name.lower():
            node.left = self._delete_recursive(node.left, visitor_name)
        elif visitor_name.lower() > node.visitor_name.lower():
            node.right = self._delete_recursive(node.right, visitor_name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.visitor_name = min_larger_node.visitor_name
            node.entry_time = min_larger_node.entry_time
            node.purpose = min_larger_node.purpose
            node.right = self._delete_recursive(node.right, min_larger_node.visitor_name)

        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, visitor_name):
        return self._search_recursive(self.root, visitor_name)

    def _search_recursive(self, node, visitor_name):
        if node is None or node.visitor_name.lower() == visitor_name.lower():
            return node
        if visitor_name.lower() < node.visitor_name.lower():
            return self._search_recursive(node.left, visitor_name)
        return self._search_recursive(node.right, visitor_name)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.get_details())
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.get_details())
            self._inorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.get_details())

    def count_entries(self):
        return self._count_recursive(self.root)

    def _count_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)

if __name__ == "__main__":
    log_book = VisitorLogBook()

    while True:
        print("\n=== VISITOR LOG BOOK MENU ===")
        print("1. Insert a log entry")
        print("2. Delete a log entry")
        print("3. Search for a log entry")
        print("4. Traverse log entries (Pre/In/Post order)")
        print("5. Count total log entries")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter visitor name: ").strip()
            time = input("Enter entry time: ").strip()
            purpose = input("Enter purpose of visit: ").strip()
            if name and time and purpose:
                log_book.insert(name, time, purpose)
                print(f"Success: Log entry added for '{name}'.")
            else:
                print("Error: All fields are required.")

        elif choice == "2":
            name = input("Enter visitor name to remove: ").strip()
            match = log_book.search(name)
            if match:
                log_book.delete(name)
                print(f"Success: Log entry for '{name}' removed.")
            else:
                print(f"Error: No log entry found for '{name}'.")

        elif choice == "3":
            name = input("Enter visitor name to search: ").strip()
            match = log_book.search(name)
            if match:
                print(f"Found Entry: {match.get_details()}")
            else:
                print(f"No entry found for visitor: '{name}'.")

        elif choice == "4":
            if log_book.count_entries() == 0:
                print("The log book is currently empty.")
                continue
                
            print("\nSelect Traversal Order:")
            print("a. Pre-order")
            print("b. In-order (Alphabetical)")
            print("c. Post-order")
            t_choice = input("Enter option (a/b/c): ").strip().lower()
            
            if t_choice == "a":
                print("\n--- Pre-order Traversal ---")
                for entry in log_book.preorder(): print(entry)
            elif t_choice == "b":
                print("\n--- In-order Traversal ---")
                for entry in log_book.inorder(): print(entry)
            elif t_choice == "c":
                print("\n--- Post-order Traversal ---")
                for entry in log_book.postorder(): print(entry)
            else:
                print("Invalid traversal selection.")

        elif choice == "5":
            print(f"Total active log entries: {log_book.count_entries()}")

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose an option from 1 to 6.")
