#widget.py
#将要被测试的类Widget
class Widget:
    def __init__(self, size = (40, 40)):
        self._size = size
    def getSize(self):
        return self._size
    def resize(self, width, height):
        if width < 0  or height < 0:
            return "illegal size"
        self._size = (width, height)
    def dispose(self):
        pass