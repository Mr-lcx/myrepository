
# 学生的课程管理 --- 选课系统
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid

class Panel_2_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_2_1')
        # 表头
        self.title=['课程号', '课程名', '任课老师', '学分', '学时', '星期几',
                    '第几节', '教室', '平时成绩占比', '期末成绩占比', '评教']
        self.data = None  # grid数据
        self.GetAllData()  # 获得开课表的所有纪录
        self.SetFont(self.font10)

        self.button_MySc = wx.Button(self, label="查看自己选课情况", pos=(200, 10), size=(150, 30))
        self.button_MySc.Bind(wx.EVT_BUTTON, self.ShowMyData)

        self.button_OtherSc = wx.Button(self, label="查看全部老师开课情况", pos=(380, 10), size=(150, 30))
        self.button_OtherSc.Bind(wx.EVT_BUTTON, self.ShowAllData)
        # 显示开课情况表格
        self.grid = MyGrid(self, self.title, self.data, pos=(10, 40), size=(650, 350), func=self.gridSelect)

        self.staticText1 = wx.StaticText(self, label="课程号", pos=(20, 400), size=(60, 32))
        self.input1 = wx.TextCtrl(self, pos=(80, 400), size=(150, 20))
        self.staticText2 = wx.StaticText(self, label="课程名", pos=(250, 400), size=(60, 32))
        self.input2 = wx.TextCtrl(self, pos=(310, 400), size=(150, 20))
        self.staticText3 = wx.StaticText(self, label="老师", pos=(480, 400), size=(60, 32))
        self.input3 = wx.TextCtrl(self, pos=(540, 400), size=(150, 20))

        self.staticText4 = wx.StaticText(self, label="学分", pos=(20, 440), size=(60, 32))
        self.input4 = wx.TextCtrl(self, pos=(80, 440), size=(150, 20))
        self.staticText5 = wx.StaticText(self, label="学时", pos=(250, 440), size=(60, 32))
        self.input5 = wx.TextCtrl(self, pos=(310, 440), size=(150, 20))
        self.staticText6 = wx.StaticText(self, label="教室", pos=(480, 440), size=(60, 32))
        self.input6 = wx.TextCtrl(self, pos=(540, 440), size=(150, 20))

        self.staticText7 = wx.StaticText(self, label="星期几", pos=(20, 480), size=(60, 32))
        self.input7 = wx.TextCtrl(self, pos=(80, 480), size=(150, 20))
        self.staticText8 = wx.StaticText(self, label="第几节", pos=(250, 480), size=(60, 32))
        self.input8 = wx.TextCtrl(self, pos=(310, 480), size=(150, 20))
        self.staticText9 = wx.StaticText(self, label="期末占比", pos=(480, 480), size=(60, 32))
        self.input9 = wx.TextCtrl(self, pos=(540, 480), size=(150, 20))

        self.status = wx.StaticText(self, label="当前未选择", pos=(670, 100), size=(130, 32))
        self.button2_2 = wx.Button(self, label="新增选课", pos=(670, 180), size=(100, 32))
        self.button3 = wx.Button(self, label="退选课程", pos=(670, 220), size=(100, 32))
        self.button4 = wx.Button(self, label="刷新", pos=(670, 260), size=(100, 32))
        self.button2_2.Bind(wx.EVT_BUTTON, self.OnNew)
        self.button3.Bind(wx.EVT_BUTTON, self.OnDelete)
        self.button4.Bind(wx.EVT_BUTTON, self.OnFlash)
        # 设置控件初始状态
        self.button3.Enabled = False  # 设置在查看所有纪录时，不能修改纪录
        self.status.SetLabel("同学你好，请选课！")

    # 点击单元格 响应：将所点击的行的内容填写到文本框中
    def gridSelect(self,event):
        print("点击单元格")
        self.input1.SetEditable(False)
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        self.input4.SetEditable(False)
        self.input5.SetEditable(False)
        self.input6.SetEditable(False)
        self.input7.SetEditable(False)
        self.input8.SetEditable(False)
        self.input9.SetEditable(False)
        # 获取行号
        row = event.GetRow()
        self.id = self.grid.GetCellValue(row, 0)
        self.status.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        self.input3.SetLabel(self.grid.GetCellValue(row, 2))
        self.input4.SetLabel(self.grid.GetCellValue(row, 3))
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))
        self.input6.SetLabel(self.grid.GetCellValue(row, 7))
        self.input7.SetLabel(self.grid.GetCellValue(row, 5))
        self.input8.SetLabel(self.grid.GetCellValue(row, 8))
        self.input9.SetLabel(self.grid.GetCellValue(row, 9))


    def ShowAllData(self,event):
        print("获得所有开课数据")
        self.button3.Enabled = False  # 设置在查看所有纪录时，不能修改纪录
        self.button2_2.Enabled=True
        self.data=self.db.GetAllClassOpen()
        self.grid.updateData(self.data)

    # 点击查看所有人的开课纪录
    def GetAllData(self):
        print("获得所有老师开课数据")
        self.data=self.db.GetAllClassOpen()

    # 点击显示自己选课纪录
    def ShowMyData(self,event):
        print("获得自己选课数据")
        self.button3.Enabled = True  # 设置在查看自己选课纪录时，能退选纪录
        self.button2_2.Enabled = False  # 设置在查看自己选课纪录时，不能添加已选课程
        print("*学号*",self.person.id)
        self.data = self.db.GetMySc(self.person.id)
        self.grid.updateData(self.data)

    # 新增开课
    def OnNew(self, event):
        objectNum = self.input1.GetValue()
        # 连接数据库
        fg = self.db.ScInsert(objectNum, self.person.id)
        if fg:
            self.success("选课成功")
            wx.MessageBox("选课成功")
            self.data = self.db.GetMySc(self.person.id)
            self.grid.updateData(self.data)
        else:
            self.success("插入失败，请检查", False)

    # 删除开课纪录
    def OnDelete(self, event):
        objectNum = self.input1.GetValue()
        if objectNum:
            fg = self.db.ScDelete(self.person.id,objectNum)
            if fg:
                self.success("退选成功！")
                wx.MessageBox("退选成功！")
                # 退选后更新表格视图
                self.data = self.db.GetMySc(self.person.id)
                self.grid.updateData(self.data)
        else:
            self.success("请选择想要退选的课程！", False)

    def OnFlash(self, event):
        self.success("窗口刷新中")

    def success(self, value, flag=True):
        self.status.SetLabel(value)
        if flag:
            self.grid.updateData(self.data)
            self.input1.Clear()
            self.input2.Clear()
            self.input3.Clear()
            self.input4.Clear()
            self.input5.Clear()
            self.input6.Clear()
            self.input7.Clear()
            self.input8.Clear()
            self.input9.Clear()
            # 设置控件初始状态

