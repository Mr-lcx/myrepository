

import wx
from Util.MyPanel import MyPanel


class Panel_5_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_5_2')

        self.input = wx.TextCtrl(self, pos=(10, 10), size=(760, 400), style=wx.TE_MULTILINE)
        self.button = wx.Button(self, label="发布", pos=(300, 420), size=(200, 60))
        self.button.Bind(wx.EVT_BUTTON, self.OnSubmit)


    def OnSubmit(self, event):
        text = self.input.GetValue()
        name = self.person.name
        self.db.noticeInsert(text, name)
        # TODO： AttributeError: 'DBManager' object has no attribute 'commit'
        # self.db.commit()
        wx.MessageBox("发布成功")
