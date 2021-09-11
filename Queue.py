class QueueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self,e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._data[0]

    def print_hi(self,name):
     print(f'Hi, {name}')

class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class QueueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.isempty():
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._front._element

    def dispaly(self):
        p = self._front
        while p:
            print(p._element,end='<--')
            p = p._next
        print()


class DeQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self,e):
        self._data.insert(0,e) #since we are passing at first part hence 0

    def addlast(self,e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print('Dequeu is Empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('Dequeu is empty')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('Dequeuis empty')
            return
        return self._data[-1]

class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class QueueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.isempty():
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._front._element

    def dispaly(self):
        p = self._front
        while p:
            print(p._element,end='<--')
            p = p._next
        print()


if __name__ == '__main__':
    Q = QueueArray()
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    print(Q._data)
    print('Length:', len(Q))
    Q.enqueue(7)
    Q.enqueue(12)
    print(Q._data)
    print(Q.dequeue())
    print(Q._data)

    print(Q.first())
    print(Q._data)

    Q.print_hi('PyCharm')

    q = QueueLinked()
    q.enqueue(5)
    q.enqueue(3)
    q.dispaly()
    print('length:', len(q))
    q.enqueue(7)
    q.enqueue(12)
    q.dispaly()
    print('Length:', len(q))
    print(q.dequeue())
    q.dispaly()
    print('Lenght:', len(q))
    print(q.first())
    q.dispaly()

    D = DeQueArray()
    D.addfirst(5)
    D.addfirst(3)
    D.addlast(7)
    D.addlast(12)
    print(D._data)
    print('Length:', len(D))
    print(D.removefirst())
    print(D.removelast())
    print(D._data)
    print('First element:', D.first())
    print('Last element:',D.last())
