
"""
    所有的grid基于此
"""
import wx
from wx.grid import Grid
from Util.MyGridTable import MyGridTable


class MyGrid(Grid):
    def __init__(self, panel, title=None, data=None, pos=None, size=None, func=None):
        super().__init__(parent=panel, pos=pos, size=size)
        self.title = title
        self.pos = pos
        self.size = size
        # 创建MyGridTable的实例作为当前对象的一个成员变量
        gridTable = MyGridTable(title, data)
        self.SetTable(gridTable, True)
        self.AutoSizeColumns()
        # 单元格左键点击事件
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, func)

    def updateData(self, data):
        self.ClearGrid()
        gridTable = MyGridTable(self.title, data)
        self.SetTable(gridTable, True)
        self.SetPosition(self.pos)
        self.SetSize(self.size)
        self.AutoSizeColumns()

    def updateData1(self, title,data):
        self.ClearGrid()
        gridTable = MyGridTable(title, data)
        self.SetTable(gridTable, True)
        self.SetPosition(self.pos)
        self.SetSize(self.size)
        self.AutoSizeColumns()

    def SetCenter(self, cols):
        pass
        # for i in range(self.GetNumberRows()):
        #     # 文本居中
        #     for j in range(self.GetNumberCols()):
        #         self.SetCellAlignment(i, j, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
