class stackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data[-1]


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class StacksLinked:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    #  S = stackArray()
    #   S.push(5)
    #  S.push(3)
    #  S.push(4)
    # print(S._data)
    # print('Length:', len(S))
    # print(S.pop())
    # print(S.isempty())
    # print(S.top())

    A = StacksLinked()
    A.push(5)
    A.push(3)
    print('Length:', len(A))
    A.display()
    print(A.pop())
    print(A.isempty())
    A.display()
    print(A.pop())
    print(A.isempty())
    A.display()
    A.push(8)
    A.push(4)
    A.push(4)
    A.push(1)
    print(A.top())
    A.display()
