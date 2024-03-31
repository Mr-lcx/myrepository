
"""
    查看公告
"""

import wx
import wx.grid
from Util.MyGrid import MyGrid
from Util.MyPanel import MyPanel


class Panel_6_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_6_2')
        self.title = ['编号', '内容', '发布者姓名', '发布时间']

        self.data = self.db.noticeSelectAll()

        self.grid = MyGrid(self, self.title, self.data, pos=(10, 10), size=(760, 500))
        rowsizeinfo = wx.grid.GridSizesInfo(40, [])  # 固定课表宽和高
        self.grid.SetRowSizes(rowsizeinfo)