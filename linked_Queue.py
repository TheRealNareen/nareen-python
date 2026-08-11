class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
    def dequeue(self):
        if self.is_empty():
            return None
        data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return data
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    def size(self):
        count=0
        current=self.front
        while current:
            count +=1
            current=current.next
        return count
    def disp(self):
        if self.is_empty():
            print("None")
            return None
        temp=self.front
        print("The queue is: ")
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        

q = Queue()
while True:
    print("\n============================")
    print("Select one of the operations:")
    print("1.Add Car.")
    print("2.Remove Car.")
    print("3.Display Queue.")
    print("4.Size of Queue.")
    print("5.Exit.")
    print("\n============================\n")
    choice=(int(input()))
    if choice == 1:
        print("Enter the number of Cars to add: ")
        t=int(input())
        for i in range(t):
            p = input("Enter Car: ")
            q.enqueue(p)
    elif choice == 2:
        print("Enter the number of Cars to Remove: ")
        tp=int(input())
        for i in range(tp):
            q.dequeue()
    elif choice == 3:
        q.disp()
    elif choice == 4:
        print("The size of the queue is: ",q.size())
    elif choice == 5:
        print("Thank you...")
        break
