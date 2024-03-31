
"""
    grid表格工具
"""

from wx.grid import GridTableBase


class MyGridTable(GridTableBase):
    def __init__(self, title, data):
        super().__init__()
        self.title = title
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.title)

    def GetValue(self, row, col):
        return self.data[row][col]

    def GetColLabelValue(self, col):
        return self.title[col]
