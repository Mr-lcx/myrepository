
"""
    所有panel基于此
"""
import wx
from Database.DBManager import DBManager as DB


class MyPanel(wx.Panel):
    # 数据库连接池
    db = None

    def __init__(self, parent, name='base'):
        super().__init__(parent=parent,
                         size=(800, 600))
        self.parent = parent
        self.person = parent.person   # TODO: 有点问题
        # 构造一个DBManger类的实例属性
        self.db = DB()

        self.font16 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font14 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font12 = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font10 = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font8 = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.font6 = wx.Font(6, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        # 调用父类Panel的设置字体方法
        self.SetFont(self.font16)
        print(name)

