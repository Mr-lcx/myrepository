
"""
    全局frame基于此
    设置了字体
    设置了db
"""

import wx
from Database.DBManager import DBManager as DB


class MyFrame(wx.Frame):
    # 数据库连接池
    db = None
    # 存放访问对象
    person = None

    def __init__(self,
                 person=None,
                 title="",
                 size=(800, 600)):
        super().__init__(parent=None,
                         title=title,
                         size=size)
        self.person = person
        self.font16 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.SetFont(self.font16)
        self.Center()

        self.db = DB()

    def OnCancel(self, event):
        pass
