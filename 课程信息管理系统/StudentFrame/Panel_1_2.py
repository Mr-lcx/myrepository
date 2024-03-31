# 学生的修改密码 面板
import wx
from Util.MyPanel import MyPanel


class Panel_1_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_1_2')

        self.staticText1 = wx.StaticText(self, label="原密码", pos=(10, 15), size=(100, 32))
        self.staticText2 = wx.StaticText(self, label="新密码", pos=(10, 55), size=(100, 32))
        self.staticText3 = wx.StaticText(self, label="确认密码", pos=(10, 95), size=(100, 32))
        self.input1 = wx.TextCtrl(self, pos=(110, 10), size=(250, 32), style=wx.TE_PASSWORD)
        self.input2 = wx.TextCtrl(self, pos=(110, 50), size=(250, 32), style=wx.TE_PASSWORD)
        self.input3 = wx.TextCtrl(self, pos=(110, 90), size=(250, 32), style=wx.TE_PASSWORD)

        self.button = wx.Button(self, label="修改", pos=(110, 130), size=(250, 64))
        self.button.Bind(wx.EVT_BUTTON, self.OnSubmit)

        self.status = wx.StaticText(self, pos=(110, 204), size=(200, 32))

    # 修改密码
    def OnSubmit(self, event):
        self.status.SetLabel("")
        if len(self.input1.GetValue()) == 0 or len(self.input2.GetValue()) == 0 or len(self.input3.GetValue()) == 0:
            self.status.SetLabel("密码不可为空")
            return
        if self.input2.GetValue() != self.input3.GetValue():
            self.status.SetLabel("两次密码不一致")
            return
        if self.GetPossWord()!=self.input1.GetValue():
            self.status.SetLabel("修改失败，请检查原密码是否输入正确")
            return

        fg = self.db.StudentUpdatePassword(self.person.id, self.input2.GetValue())
        if fg :
            self.status.SetLabel("修改成功")
            self.input1.Clear()
            self.input2.Clear()
            self.input3.Clear()
        return


    def GetPossWord(self):
        result=self.db.GetStudentOne(self.person.id)
        return result[3]

