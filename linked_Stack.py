class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
stack = Stack()
while True:
    print("\n============================")
    print("Select one of the operations:")
    print("1.Add book.")
    print("2.Remove book.")
    print("3.Peek Stack.")
    print("4.Is the stack empty?.")
    print("5.Exit.")
    print("\n============================\n")
    choice=(int(input()))
    if choice == 1:
        print("Enter the number of Books to add: ")
        t=int(input())
        for i in range(t):
          p = input("Enter a books to push: ")
          stack.push(p)
    elif choice == 2:
        print("Enter the number of books to Remove: ")
        tp=int(input())
        for i in range(tp):
            stack.pop()
    elif choice == 3:
        print("Top of stack: ", stack.peek())
    elif choice == 4:
        print("Is the stack empty?: ", stack.is_empty())
    elif choice == 5:
        print("Thank you...")
        break

