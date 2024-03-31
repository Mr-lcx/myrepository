# 发布公告部分

import wx
from Util.MyPanel import MyPanel


class Panel_6_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_6_1')

        self.input = wx.TextCtrl(self, pos=(10, 10), size=(760, 400), style=wx.TE_MULTILINE)
        self.button = wx.Button(self, label="发布", pos=(300, 420), size=(200, 60))
        self.button.Bind(wx.EVT_BUTTON, self.OnSubmit)

    # 点击发布 公告按钮 添加到数据库
    def OnSubmit(self, event):
        text = self.input.GetValue()
        name = self.person.name
        self.db.noticeInsert(text, name)
        wx.MessageBox("发布成功")
