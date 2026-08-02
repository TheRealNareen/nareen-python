class Node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None
class polynomial:
    def __init__(self):
        self.head = None
    def insert(self,coeff,exp):
        new_node = Node(coeff,exp)
        if self.head is None:
            self.head = new_node
            return
        current=self.head
        while current:
            if current.exp == exp:
                current.coeff += coeff
                return
            if current.next is None:
                break
            current = current.next
        current.next = new_node
    def delete(self,exp):
        current = self.head
        previous = None
        while current:
            if current.exp == exp:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
    def display(self):
        current = self.head
        terms = []
        while current:
            if current.exp == 0:
                terms.append(f'{current.coeff}')
            elif current.exp == 1:
                    terms.append(f'{current.coeff}x')
            else:
                    terms.append(f'{current.coeff}x^{current.exp}')
            current = current.next
        print(' + '.join(terms) if terms else'0')
    def merge(self,poly2):
        result = polynomial()
        combined = {}
        current = self.head
        while current:
            combined[current.exp] = combined.get(current.exp, 0) + current.coeff
            current = current.next
           
        current = poly2.head
        while current:
            combined[current.exp] = combined.get(current.exp, 0) + current.coeff
            current = current.next
           
        for exp in sorted(combined.keys(), reverse=True):
            result.insert(combined[exp], exp)
        return result
   
p1 = polynomial()
p1.insert(5,4)
p1.insert(3,2)
p1.insert(2,0)
p1.display()

p2 = polynomial()
p2.insert(4,4)
p2.insert(7,1)
p2.insert(8,0)
p2.display()

p3 = p1.merge(p2)
p3.display()

p1.delete(2)
p1.display()