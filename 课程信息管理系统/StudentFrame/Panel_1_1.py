# 学生的个人信息窗口

import wx
from Util.MyPanel import MyPanel

class Panel_1_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_1_1')

        staticText = wx.StaticText(self, pos=(10, 10), size=(300, 32))
        s = "欢迎您：   学号: %s , 姓名: %s ,性别：%s  身份: %s" % (self.person.id,self.person.name, self.person.sex, self.person.type)
        staticText.SetLabel(s)

        self.type = self.person.type
        self.id = self.person.id
        self.statusPos=330

        title = ['教工号', '姓名', '性别', '班级', '所在学院']

        self.staticText1 = wx.StaticText(self, label=title[0], pos=(10, 55), size=(100, 32))
        self.staticText2 = wx.StaticText(self, label=title[1], pos=(10, 95), size=(100, 32))
        self.staticText3 = wx.StaticText(self, label=title[2], pos=(10, 135), size=(100, 32))
        self.staticText4 = wx.StaticText(self, label=title[3], pos=(10, 175), size=(100, 32))
        self.staticText5 = wx.StaticText(self, label=title[4], pos=(10, 215), size=(100, 32))
        self.input1 = wx.TextCtrl(self, pos=(120, 50), size=(200, 32),value=self.person.id)
        self.input2 = wx.TextCtrl(self, pos=(120, 90), size=(200, 32),value=self.person.name)
        self.input3 = wx.TextCtrl(self, pos=(120, 130), size=(200, 32),value=self.person.sex)
        self.input4 = wx.TextCtrl(self, pos=(120, 170), size=(200, 32),value=self.person.classes)
        self.input5 = wx.TextCtrl(self, pos=(120, 210), size=(200, 32),value=self.person.xueyuan)
        self.input1.SetEditable(False)
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        # 修改按钮
        self.button = wx.Button(self, label="修改", pos=(120, 270), size=(200, 32))
        self.button.Bind(wx.EVT_BUTTON, self.OnSubmit)
        # 显示修改状态
        self.status = wx.StaticText(self, pos=(self.statusPos, 270), size=(200, 32))

    # 学生提交修改信息
    def OnSubmit(self, event):
        classes = self.input4.GetValue()
        xueyuan=self.input5.GetValue()
        fg = self.db.studentUpdata(self.id, classes,xueyuan)
        if fg: # 修改成功
            self.status.SetLabel("修改成功")
            self.statusPos=self.statusPos+50 # 为了防止修改是否成功不名校，所有这里偏移一下位置
            self.status.SetPosition((self.statusPos, 270))
            self.person.classes=classes
            self.person.xueyuan=xueyuan
            self.input4.SetValue(classes)
            self.input5.SetValue(xueyuan)