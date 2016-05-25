#static.py

import unittest

from com.python.pyunit.Widget import Widget
#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget()
        self.assertEqual(widget.getSize(), (40, 40))
#测试
if __name__ == "__main__":
    testCase = WidgetTestCase()
    testCase.runTest()