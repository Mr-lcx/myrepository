

import wx

from Util.MyGrid import MyGrid
from Util.MyPanel import MyPanel


class Panel_5_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_5_1')

        self.title = ['编号', '内容', '姓名', '发布时间']

        self.data = self.db.noticeSelectAll()

        self.grid = MyGrid(self, self.title, self.data, pos=(10, 10), size=(760, 500))