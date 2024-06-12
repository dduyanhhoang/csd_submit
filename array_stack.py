from dynamic_array import DynamicArray
from exception import Empty


class ArrayStack:
    def __init__(self):
        self._data = DynamicArray()

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, e) -> None:
        self._data.append(e)

    def top(self) -> any:
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self) -> any:
        if self.is_empty():
            raise Empty('Stack is empty')
        top = self._data[self._data._index - 1]
        self._data[self._data._index - 1] = None
        self._data._index -= 1
        return top
