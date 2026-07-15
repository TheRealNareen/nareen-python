
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def display(head):
    temp = head
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next
    print("None")
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next=n2
n2.next=n3
print("Orginal Linked List")
head=n1
display(head)

print("\nInsertion at begining")
new_node=Node(5)
new_node.next = head
head = new_node
display(head)

print("\nInsertion in the middle")
new_node1=Node(25)
temp=head
while temp.data!=20:
    temp=temp.next
new_node1.next=temp.next
temp.next=new_node1
display(head)

print("\nInsertion at end")
new_node2=Node(40)
temp=head
while temp.next:
    temp=temp.next
temp.next=new_node2
display(head)

print("\nDeletion at beginning")
head=head.next
display(head)

print("\nDeletion in the middle")
temp=head
while temp.next.data!=25:
    temp=temp.next
temp.next=temp.next.next
display(head)

print("\nDeletion at end")
temp=head
while temp.next.next:
    temp=temp.next
temp.next=None
display(head)
