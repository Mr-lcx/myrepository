
# 教师的课程管理 --- 开课管理
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid

class Panel_3_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_3_1')
        # 表头
        self.title=['课程号', '课程名', '任课老师', '学分', '学时', '星期几',
                    '第几节', '教室', '平时成绩占比', '期末成绩占比', '评教']
        self.Week=['星期一','星期二','星期三','星期四','星期五']
        self.Section=['第一大节','第二大节','第三大节','第四大节']
        self.data = None  # grid数据
        self.GetAllData()  # 获得开课表的所有纪录
        self.SetFont(self.font10)

        self.button_MySc = wx.Button(self, label="查看自己开课情况", pos=(200, 10), size=(150, 30))
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
        self.input7 = wx.Choice(self, pos=(80, 480), size=(150, 20))
        self.input7.Set(self.Week)
        self.staticText8 = wx.StaticText(self, label="第几节", pos=(250, 480), size=(60, 32))
        self.input8 = wx.Choice(self, pos=(310, 480), size=(150, 20))
        self.input8.Set(self.Section)
        self.staticText9 = wx.StaticText(self, label="期末占比", pos=(480, 480), size=(60, 32))
        self.input9 = wx.TextCtrl(self, pos=(540, 480), size=(150, 20))

        self.status = wx.StaticText(self, label="当前未选择", pos=(670, 100), size=(130, 32))
        self.button1 = wx.Button(self, label="切换状态", pos=(670, 140), size=(100, 32))
        self.button2_1 = wx.Button(self, label="修改", pos=(670, 180), size=(100, 32))
        self.button2_2 = wx.Button(self, label="新增", pos=(670, 180), size=(100, 32))
        self.flag = True  # 默认为新增状态
        self.button2_1.Hide()
        self.button3 = wx.Button(self, label="删除", pos=(670, 220), size=(100, 32))
        self.button4 = wx.Button(self, label="刷新", pos=(670, 260), size=(100, 32))
        self.button1.Bind(wx.EVT_BUTTON, self.OnStatus)
        self.button2_1.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.button2_2.Bind(wx.EVT_BUTTON, self.OnNew)
        self.button3.Bind(wx.EVT_BUTTON, self.OnDelete)
        self.button4.Bind(wx.EVT_BUTTON, self.OnFlash)
        # 设置控件初始状态
        self.button2_1.Hide()
        self.input1.SetEditable(False)
        self.flag = True  # 初始True为新增
        self.status.SetLabel("请添加开课！")

    # 点击单元格 响应：将所点击的行的内容填写到文本框中
    def gridSelect(self,event):
        print("点击单元格")
        # 自动切换修改状态
        self.flag = False
        self.button2_1.Show()  # 隐藏新增
        self.button2_2.Hide()  # 打开修改
        self.input1.SetEditable(False)
        self.input2.SetEditable(True)
        self.input3.SetEditable(False)
        self.input4.SetEditable(True)
        self.input5.SetEditable(True)
        self.input6.SetEditable(True)
        self.input9.SetEditable(True)
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
        self.input9.SetLabel(self.grid.GetCellValue(row, 9))

        # 处理input7
        week = self.grid.GetCellValue(row, 5)
        weekId = self.weekIndex(week)  # 获取学院编号
        self.input7.SetSelection(weekId-1)
        # 处理input8
        classes = self.grid.GetCellValue(row, 5)
        classesId = self.weekIndex(classes)  # 获取学院编号
        self.input8.SetSelection(classesId-1)

        # event.Skip()

    def ShowAllData(self,event):
        print("获得所有开课数据")
        self.button2_1.Enabled = False  # 设置在查看所有纪录时，不能删除纪录
        self.button3.Enabled = False  # 设置在查看所有纪录时，不能修改纪录
        self.data=self.db.GetAllClassOpen()
        self.grid.updateData(self.data)
    # 点击查看所有人的开课纪录
    def GetAllData(self):
        print("获得所有开课数据")
        self.data=self.db.GetAllClassOpen()
    # 点击显示自己开课纪录
    def ShowMyData(self,event):
        print("获得自己开课数据")
        self.button2_1.Enabled = True  # 设置在查看所有纪录时，能删除纪录
        self.button3.Enabled = True  # 设置在查看所有纪录时，能修改纪录
        self.data = self.db.GetMyClassOpen(self.person.name)
        self.grid.updateData(self.data)

    # 状态的切换
    def OnStatus(self, event):
        self.flag = not self.flag
        if self.flag:  # 新增
            self.button2_1.Hide()  # 隐藏修改
            self.button2_2.Show()  # 打开新增
            self.status.SetLabel("请添加开课！")
            self.input1.SetValue("自动生成")
            self.input2.Clear()
            self.input3.SetValue(self.person.name)
            self.input4.Clear()
            self.input5.Clear()
            self.input6.Clear()
            self.input9.Clear()
            self.input1.SetEditable(False)
            self.input2.SetEditable(True)
            self.input3.SetEditable(False)
            self.input4.SetEditable(True)
            self.input5.SetEditable(True)
            self.input6.SetEditable(True)
            self.input9.SetEditable(True)
        else:
            self.button2_1.Show()  # 隐藏新增
            self.button2_2.Hide()  # 打开修改
            self.status.SetLabel("请选择班级")
            self.input1.SetLabel("")
            self.input2.SetLabel("")
            self.input3.SetLabel("")
            self.input4.SetLabel("")
            self.input5.SetLabel("")
            self.input6.SetLabel("")
            self.input1.SetEditable(False)
            self.input2.SetEditable(False)
            self.input3.Clear()
            self.input4.Clear()
            self.input5.Clear()
            self.input6.SetEditable(False)

    # 编辑开课纪录
    def OnEdit(self, event):
        objectNum = self.input1.GetValue()
        objectName = self.input2.GetValue()
        xuefen=self.input4.GetValue()
        xueshi = self.input5.GetValue()
        jiaoshi = self.input6.GetValue()
        week = self.input7.GetString(self.input7.GetSelection())
        classes = self.input8.GetString(self.input8.GetSelection())
        qimozhanbi=self.input9.GetValue()
        if len(objectName) == 0:
            self.success("课程名不可为空", False)
            return
        if not xuefen.isdecimal():
            self.success("学分要为数字", False)
            return
        if not xueshi.isdecimal():
            self.success("学时要为数字", False)
            return
        if len(jiaoshi) == 0:
            self.success("教室不能为空", False)
            return
        if len(week) == 0:
            self.success("请选择第几个星期", False)
            return
        if len(classes) == 0:
            self.success("请选择第几节课", False)
            return
        if not qimozhanbi.isdecimal():
            self.success("期末占比要为数字", False)
            return
        # 连接数据库
        objectNum=int(objectNum)
        fg = self.db.ClassesUpdate(objectNum,objectName,self.person.name,xuefen,xueshi,jiaoshi,week,classes,qimozhanbi)
        if fg:
            self.success("修改成功")
            self.data = self.db.GetMyClassOpen(self.person.name)
            self.grid.updateData(self.data)
        else:
            self.success("修改失败，请检查", False)

    # 新增开课
    def OnNew(self, event):

        objectName = self.input2.GetValue()
        xuefen = self.input4.GetValue()
        xueshi = self.input5.GetValue()
        jiaoshi = self.input6.GetValue()
        week = self.input7.GetString(self.input7.GetSelection())
        classes = self.input8.GetString(self.input8.GetSelection())
        qimozhanbi = self.input9.GetValue()
        self.input3.SetEditable(False)
        if len(objectName) == 0:
            self.success("课程名不可为空", False)
            return
        if not xuefen.isdecimal():
            self.success("学分要为数字", False)
            return
        if not xueshi.isdecimal():
            self.success("学时要为数字", False)
            return
        if len(jiaoshi) == 0:
            self.success("教室不能为空", False)
            return
        if len(week) == 0:
            self.success("请选择第几个星期", False)
            return
        if len(classes) == 0:
            self.success("请选择第几节课", False)
            return
        if not qimozhanbi.isdecimal():
            self.success("期末占比要为数字", False)
            return
        # 连接数据库
        fg = self.db.ClassesInsert(objectName, self.person.name, xuefen, xueshi, jiaoshi, week, classes, qimozhanbi)
        if fg:
            self.success("插入成功")
            self.data = self.db.GetMyClassOpen(self.person.name)
            self.grid.updateData(self.data)

        else:
            self.success("插入失败，请检查", False)

    # 删除开课纪录
    def OnDelete(self, event):
        objectNum = self.input1.GetValue()
        if objectNum:
            fg = self.db.ClassesDelete(objectNum)
            if fg:
                self.success("删除成功")
                # 删除后更新表格视图
                self.data = self.db.GetMyClassOpen(self.person.name)
                self.grid.updateData(self.data)
        else:
            self.success("请选择想要删除的项", False)

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
            self.input9.Clear()
            # 设置控件初始状态
            self.button2_1.Hide()
            self.button2_2.Show()
            self.flag = True  # 初始为新增
            # if "刷新" not in value:
            #     self.status.SetLabel("新增开课！")

    def weekIndex(self,week):
        if week=="星期一":
            return 1
        if week=="星期二":
            return 2
        if week=="星期三":
            return 3
        if week=="星期四":
            return 4
        if week=="星期五":
            return 5
    def classesIndex(self,week):
        if week=="第一节":
            return 1
        if week=="第二节":
            return 2
        if week=="第三节":
            return 3
        if week=="第四节":
            return 4
        if week=="第五节":
            return 5
