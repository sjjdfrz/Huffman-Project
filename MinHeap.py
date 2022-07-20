class MinHeap:

    def __init__(self):

        self.heap = []

    def parent(self, pos):
        return int((pos - 1) / 2)

    def leftChild(self, pos):
        return (2 * pos) + 1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, pos):
        return (len(self.heap) // 2) <= pos <= len(self.heap)

    def swap(self, position1, position2):
        self.heap[position1], self.heap[position2] = self.heap[position2], self.heap[position1]

    def minHeapify(self, position):

        if not self.isLeaf(position):

            if self.rightChild(position) < len(self.heap):

                if (self.heap[position].key > self.heap[self.leftChild(position)].key or
                        self.heap[position].key > self.heap[self.rightChild(position)].key):

                    if self.heap[self.leftChild(position)].key < self.heap[self.rightChild(position)].key:
                        self.swap(position, self.leftChild(position))
                        self.minHeapify(self.leftChild(position))

                    else:
                        self.swap(position, self.rightChild(position))
                        self.minHeapify(self.rightChild(position))
            else:
                if self.heap[position].key > self.heap[self.leftChild(position)].key:
                    self.swap(position, self.leftChild(position))
                    self.minHeapify(self.leftChild(position))

    def insert(self, element):

        current = len(self.heap)
        self.heap.append(element)

        while self.heap[current].key < self.heap[self.parent(current)].key:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.minHeapify(0)
        return popped
