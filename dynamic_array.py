from array import Array


class DynamicArray(Array):
    def __init__(self, cap: int = 1):
        super().__init__(cap)

    def _resize(self, nc) -> None:
        temp_arr = self._make_array(nc)
        for e in range(self.index):
            temp_arr[e] = self._array[e]
        self._array = temp_arr
        self._capacity = nc

    def append(self, e):
        if self._index == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._index] = e
        self._index += 1
