class Node:

    def __init__(self, character, key, leftChild=None, rightChild=None, middleChild=None):

        self.key = key
        self.character = character
        self.leftChild = leftChild
        self.middleChild = middleChild
        self.rightChild = rightChild
        self.binary = ''
