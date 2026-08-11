queue=[None]*6
front=-1
rear=-1
def enqueue(x):
    global front,rear
    if rear ==5:
        print("Queue Overflow")
    else:
        if front==-1:
            front=0
        rear += 1
        queue[rear]=x
        print("Inserted: ",x)
def dequeue():
    global front,rear
    if front==-1 or front >rear:
        print("Queue Underflow")
    else:
        print("Deleted: ",queue[front])
        front += 1
def display():
    if front == -1 or front > rear:
        print("Queue is Empty.")
    else:
        print("Queue:",queue[front:rear+1])

while True:
    print("\n============================")
    print("Select one of the operations:")
    print("1.Add Car.")
    print("2.Remove Car.")
    print("3.Display Queue.")
    print("4.Exit.")
    print("\n============================\n")
    choice=(int(input()))
    if choice == 1:
        print("Enter the number of Cars to add: ")
        t=int(input())
        for i in range(t):
            p = input("Enter Car: ")
            enqueue(p)
    elif choice == 2:
        print("Enter the number of Cars to Remove: ")
        tp=int(input())
        for i in range(tp):
            dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Thank you...")
        break

