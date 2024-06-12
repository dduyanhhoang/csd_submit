from dynamic_array import DynamicArray
from exception import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = DynamicArray()
        self._size = 0
        self._front = 0

    def __str__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queu is tempys")
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        front = self._data[0]
        self._data[0] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return front

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self.data = DynamicArray(cap)
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
