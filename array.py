import ctypes


class Array():
    def __init__(self, cappacity: int):
        self._index = 0
        self.cappacity = cappacity
        self._array = self._make_array(cappacity)

    @property
    def index(self):
        return self._index

    @property
    def array(self):
        return self._array

    def _make_array(self, cap):
        return (cap * ctypes.py_object)()

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('index must be an int')
        elif not 0 <= index < self.index:
            raise IndexError('invalid index')
        return self.array[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError('index must be an int')
        elif not 0 <= index < self.index:
            raise IndexError('invalid index')
        self._array[index] = value

    def __len__(self) -> int:
        return self.index

    def __str__(self) -> str:
        arr_str = "["

        for i in range(self._index):
            arr_str += ' ' + str(self._array[i]) + ','
        arr_str = arr_str.rstrip(',')
        arr_str += ' ]'

        return arr_str
