from MinHeap import *
from Node import *

def printNodes(node: Node, value1=''):
    value2 = value1 + str(node.binary)

    if node.leftChild:
        printNodes(node.leftChild, value2)

    if node.rightChild:
        printNodes(node.rightChild, value2)

    if not node.leftChild and not node.rightChild:
        print(f"{node.character}: {len(value2)}")


nodes = MinHeap()
print('Please enter the characters: ', end='')
characters = input().split(' ')
print('Please enter the frequency of characters: ', end='')
frequency = list(map(int, input().split(' ')))
inputList = list(zip(characters, frequency))

for x, y in inputList:
    nodes.insert(Node(x, y))

while len(nodes.heap) != 1:

    left = nodes.remove()
    right = nodes.remove()

    left.binary = 0
    right.binary = 1

    newNode = Node('', left.key + right.key, left, right)

    nodes.insert(newNode)

printNodes(nodes.heap[0])
