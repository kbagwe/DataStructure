from queue import Queue
import heapq

stack = []


def reverse(q):
    while not q.empty():
        stack.append(q.get())
    print(stack)
    while len(stack) != 0:
        q.put(stack.pop())
    while not q.empty():
        print('Reverse:',q.get(), end='-->')
    print('\n')


heap = [4, 5, 6, 15, 9, 7, 20, 16, 25, 14, 12, 11, 2]
heapq.heapify(heap)
print(heap)
res = []


def removeElem(key):
    while heap[0] <= key:
        print(heap)
        res.append(heapq.heappop(heap))
    return res


class treeNode:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


def isSame(n1, n2):
    if (n1 == None and n2 == None):
        return True
    elif (n1 != None and n2 == None):
        return False
    elif (n1 == None and n2 != None):
        return False
    else:
        if (n1.element == n2.element and
                isSame(n1.left, n2.left)
                and isSame(n1.right, n2.right)):
            return True
        else:
            return False


print(removeElem(7))

n1 = treeNode(1)
n2 = treeNode(1)
n1.left = treeNode(2)
n1.right = treeNode(3)

n2.left = treeNode('None')
n2.right = treeNode(3)

if (isSame(n1, n2)):
    print("Same Binary Tree")
else:
    print("Different Binary Tree")

    q = Queue()
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)
    reverse(q)
