import wx
from Util.MyFrame import MyFrame


class Register(MyFrame):
    def __init__(self, person):
        super().__init__(title="新用户注册",
                         size=(350, 600))
        font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.flag = person  # 这个用来纪录注册的对象是什么
        panel = wx.Panel(self)
        # 用户名
        staticName = wx.StaticText(panel, label='用户名:')
        self.textName = wx.TextCtrl(panel, value="")
        self.textName.SetFont(font11)
        # 姓名
        Name1 = wx.StaticText(panel, label='姓名:')
        self.Name1 = wx.TextCtrl(panel, value="")
        self.Name1.SetFont(font11)

        # 性别
        Sex = wx.StaticText(panel, label='选择性别:')
        self.Sex = wx.Choice(panel)
        self.Sex.SetFont(font11)
        self.Sex.Set(["男", "女"])
        # 密码
        staticPassword = wx.StaticText(panel, label='  密码:')
        self.textPassword = wx.TextCtrl(panel, value="", style=wx.TE_PASSWORD)
        self.textPassword.SetFont(font11)

        # 找回密码
        Password = wx.StaticText(panel, label='密保:')
        self.Password = wx.TextCtrl(panel, value="")
        self.Password.SetFont(font11)

        # 学院
        Xueyuan = wx.StaticText(panel, label='学院:')
        self.Xueyuan = wx.TextCtrl(panel, value="")
        self.Xueyuan.SetFont(font11)

        # 班级或联系方式
        Classes = wx.StaticText(panel, label='班级:')
        self.Classes = wx.TextCtrl(panel, value="")
        self.Classes.SetFont(font11)

        # 按钮
        buttonOK = wx.Button(panel, label="注册")
        buttonOK.Bind(wx.EVT_BUTTON, self.OnOk)

        # 用户名横向布局
        boxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer1.Add(staticName, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer1.Add(self.textName, 1)
        # 姓名横向布局
        boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer2.Add(Name1, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer2.Add(self.Name1, 1)
        # 性别横向布局
        boxSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer3.Add(Sex, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer3.Add(self.Sex, 1)
        # 密码横向布局
        boxSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer4.Add(staticPassword, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer4.Add(self.textPassword, 1)
        # 找回密码横向布局
        boxSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer5.Add(Password, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer5.Add(self.Password, 1)
        # 学院横向布局
        boxSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer6.Add(Xueyuan, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer6.Add(self.Xueyuan, 1)
        # 班级或者联系方式横向布局
        boxSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer7.Add(Classes, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer7.Add(self.Classes, 1)

        boxSizer8 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer8.Add(buttonOK, 1)

        if person == "student":
            Classes.SetLabel("班级：")
        else:
            Classes.SetLabel("联系方式：")

        # 窗口纵向布局
        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        mainBoxSizer.Add(boxSizer1, 1, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        mainBoxSizer.Add(boxSizer2, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer3, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer4, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer5, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer6, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer7, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer8, 1, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        panel.SetSizer(mainBoxSizer)

    def OnOk(self, event):
        id = self.textName.GetValue()
        name = self.Name1.GetValue()
        sex = self.Sex.GetString(self.Sex.GetSelection())
        password1 = self.textPassword.GetValue()
        password2 = self.Password.GetValue()
        xueyuan = self.Xueyuan.GetValue()
        classes = self.Classes.GetValue()

        if self.flag == "teacher":
            fg = self.db.InsertTeacher(id, name, sex, password1, password2, xueyuan, classes)
        else:
            fg = self.db.InsertStudent(id, name, sex, password1, password2, xueyuan, classes)
        if fg:  # 注册成功！
            wx.MessageBox("注册成功！")
            self.Close()
        else:
            wx.MessageBox("用户已存在！")
