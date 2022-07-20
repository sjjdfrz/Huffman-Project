from MinHeap import *
from Node import *


def printNodes(node, value1=''):
    value2 = value1 + str(node.binary)

    if node.leftChild:
        printNodes(node.leftChild, value2)
    if node.middleChild:
        printNodes(node.middleChild, value2)
    if node.rightChild:
        printNodes(node.rightChild, value2)

    if not node.leftChild and not node.middleChild and not node.rightChild:
        if node.character != '?':
            print(f"{node.character}: {len(value2)}")


nodes = MinHeap()
print('Please enter the characters: ', end='')
characters = input().split(' ')
print('Please enter the frequency of characters: ', end='')
frequency = list(map(int, input().split(' ')))
inputList = list(zip(characters, frequency))

for x, y in inputList:
    nodes.insert(Node(x, y))

if len(nodes.heap) % 2 == 0:
    nodes.insert(Node('?', 0))

while len(nodes.heap) != 1:
    left = nodes.remove()
    middle = nodes.remove()
    right = nodes.remove()

    left.binary = 0
    middle.binary = 1
    right.binary = 2

    newNode = Node('', left.key + middle.key + right.key, left, middleChild=middle, rightChild=right)

    nodes.insert(newNode)

printNodes(nodes.heap[0])
