

import wx
from Util.MyPanel import MyPanel


class Panel_2_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_2_1')

        staticText = wx.StaticText(self, pos=(10, 10), size=(300, 32))
        s = "欢迎您：编号: %s , 姓名: %s ,身份: %s" % (self.person.id, self.person.name, self.person.type)
        staticText.SetLabel(s)

        self.type = self.person.type
        self.id = self.person.id

        if self.type is 'student':
            title = ['联系方式', '学院', '学系', '班级', '班主任']
        elif self.type is 'teacher':
            title = ['联系方式', '学院', '学系', '', '']
        else:
            title = ['联系方式', '', '', '', '']
        self.status = wx.StaticText(self, pos=(330, 55), size=(200, 32))
        self.staticText1 = wx.StaticText(self, label=title[0], pos=(10, 55), size=(100, 32))
        self.staticText2 = wx.StaticText(self, label=title[1], pos=(10, 95), size=(100, 32))
        self.staticText3 = wx.StaticText(self, label=title[2], pos=(10, 135), size=(100, 32))
        self.staticText4 = wx.StaticText(self, label=title[3], pos=(10, 175), size=(100, 32))
        self.staticText5 = wx.StaticText(self, label=title[4], pos=(10, 215), size=(100, 32))
        self.input1 = wx.TextCtrl(self, pos=(120, 50), size=(200, 32))
        self.input2 = wx.TextCtrl(self, pos=(120, 90), size=(200, 32))
        self.input3 = wx.TextCtrl(self, pos=(120, 130), size=(200, 32))
        self.input4 = wx.TextCtrl(self, pos=(120, 170), size=(200, 32))
        self.input5 = wx.TextCtrl(self, pos=(120, 210), size=(200, 32))
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        self.input4.SetEditable(False)
        self.input5.SetEditable(False)

        self.button = wx.Button(self, label="修改", pos=(120, 250), size=(200, 32))
        self.button.Bind(wx.EVT_BUTTON, self.OnSubmit)

        adminEntity = self.db.adminSelectById(self.person.id)
        input_phone = adminEntity[3]
        self.input1.SetValue(input_phone)
        self.input2.Hide()
        self.input3.Hide()
        self.input4.Hide()
        self.input5.Hide()
        self.button.SetPosition((120, 90))

    def OnSubmit(self, event):
        phone = self.input1.GetValue()
        # TODO：'DBManager' object has no attribute 'adminUpdatePhone'
        i = self.db.adminUpdatePhone(self.id, phone)
        self.db.commit()
        if i > 0:
            self.status.SetLabel("修改成功")
