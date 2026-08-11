class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)
myStack = Stack()
while True:
    print("\n============================")
    print("Select one of the operations:")
    print("1.Add book.")
    print("2.Remove book.")
    print("3.Display Stack.")
    print("4.Size of Stack.")
    print("5.Exit.")
    print("\n============================\n")
    choice=(int(input()))
    if choice == 1:
        print("Enter the number of Books to add: ")
        t=int(input())
        for i in range(t):
          p = input("Enter a books to push: ")
          myStack.push(p)
    elif choice == 2:
        print("Enter the number of books to Remove: ")
        tp=int(input())
        for i in range(tp):
            myStack.pop()
    elif choice == 3:
        print("Stack: ", myStack.stack)
    elif choice == 4:
        print("Size: ", myStack.size())
    elif choice == 5:
        print("Thank you...")
        break


