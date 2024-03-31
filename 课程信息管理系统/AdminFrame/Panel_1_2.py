

import wx

from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid


class Panel_1_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_1_2')
        # super(CNN, self).init()
        # 组织数据
        self.title = ['编号', '名称', '学院编号', '学院', '领导编号', '领导']
        self.data = None  # grid数据
        self.collegeNameList = None  # 学院下拉菜单
        self.collegeId = None  # 当前选择学院id
        self.leaderNameList = None  # 教师下拉菜单
        self.leaderId = None  # 当前选择教师id
        self.id = None  # 当前选择grid
        self.GetData()

        self.SetFont(self.font12)

        self.grid = MyGrid(self, self.title, self.data, pos=(10, 10), size=(450, 500), func=self.gridSelect)
        self.grid.HideCol(2)
        self.grid.HideCol(4)

        self.staticText1 = wx.StaticText(self, label=self.title[0], pos=(500, 40), size=(45, 32))
        self.staticText2 = wx.StaticText(self, label=self.title[1], pos=(500, 80), size=(45, 32))
        self.staticText3 = wx.StaticText(self, label=self.title[3], pos=(500, 120), size=(45, 32))
        self.staticText4 = wx.StaticText(self, label=self.title[5], pos=(500, 160), size=(45, 32))
        self.input1 = wx.TextCtrl(self, pos=(560, 38), size=(170, 32))
        self.input2 = wx.TextCtrl(self, pos=(560, 78), size=(170, 32))
        self.input3 = wx.Choice(self, pos=(560, 118), size=(170, 32))
        self.input4 = wx.Choice(self, pos=(560, 158), size=(170, 32))
        if self.collegeNameList is not None:
            self.input3.Set(self.collegeNameList)
        if self.leaderNameList is not None:
            self.input4.Set(self.leaderNameList)
        self.input3.Bind(wx.EVT_CHOICE, self.OnCollegeChoice)
        self.input4.Bind(wx.EVT_CHOICE, self.OnLeaderChoice)
        self.status = wx.StaticText(self, label="当前未选择", pos=(500, 200), size=(130, 32))
        self.button1 = wx.Button(self, label="切换状态", pos=(500, 240), size=(100, 32))
        self.button2_1 = wx.Button(self, label="修改", pos=(620, 240), size=(100, 32))
        self.button2_2 = wx.Button(self, label="新增", pos=(620, 240), size=(100, 32))
        self.flag = True  # 默认为新增状态
        self.button2_1.Hide()
        self.button3 = wx.Button(self, label="删除", pos=(500, 280), size=(100, 32))
        self.button4 = wx.Button(self, label="刷新", pos=(620, 280), size=(100, 32))
        self.button1.Bind(wx.EVT_BUTTON, self.OnStatus)
        self.button2_1.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.button2_2.Bind(wx.EVT_BUTTON, self.OnNew)
        self.button3.Bind(wx.EVT_BUTTON, self.OnDelete)
        self.button4.Bind(wx.EVT_BUTTON, self.OnFlash)
        # 设置控件初始状态
        self.button2_1.Hide()
        self.flag = True  # 初始为新增
        self.status.SetLabel("请录入学系")

    def GetData(self):
        deptListTmp = self.db.departmentSelectAll()
        deptList = []
        if len(deptListTmp) > 0:
            for dept in deptListTmp:
                college = self.db.collegeSelectById(dept[2])
                teacher = self.db.teacherSelectById(dept[3])
                deptList.append([
                    dept[0],
                    dept[1],
                    college[0],
                    college[1],
                    teacher[0],
                    teacher[1]
                ])
            self.data = deptList
        self.collegeNameList = self.db.collegeSelectAllName()
        if len(self.collegeNameList) > 0:
            self.collegeId = self.db.collegeSelectIdByName(self.collegeNameList[0])
            lst = self.db.TeacherSelectAllNameByCollegeId(self.collegeId)
            if lst is not False:
                self.leaderNameList = list(lst)
            else:
                self.leaderNameList = None

    def gridSelect(self, event):
        # 自动切换修改状态
        self.flag = False
        self.button2_1.Show()  # 隐藏新增
        self.button2_2.Hide()  # 打开修改
        self.input1.SetEditable(True)
        self.input2.SetEditable(True)

        row = event.GetRow()
        self.id = self.grid.GetCellValue(row, 0)
        self.status.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        # 处理input3
        tmp = self.grid.GetCellValue(row, 3)
        index = 0
        for i in range(len(self.collegeNameList)):
            if self.collegeNameList[i] == tmp:
                index = i
                break
        self.input3.SetSelection(index)
        # 处理input4
        self.leaderId = None
        self.collegeId = self.grid.GetCellValue(row, 2)  # 获取学院编号
        self.leaderNameList = self.db.TeacherSelectAllNameByCollegeId(self.collegeId)  # 从数据库获取教师列表
        if self.leaderNameList is not False:
            self.input4.Set(self.leaderNameList)
        else:
            self.input4.Clear()
        # 如果有姓名 设置index
        tmp = self.grid.GetCellValue(row, 5)  # 获取姓名
        if tmp is not "":
            for i in range(len(self.leaderNameList)):
                if self.leaderNameList[i] == tmp:
                    self.input4.SetSelection(i)
                    self.leaderId = self.grid.GetCellValue(row, 4)
                    break
        event.Skip()

    def OnCollegeChoice(self, event):
        name = event.GetString()
        self.collegeId = self.db.collegeSelectIdByName(name)  # 获取学院id
        self.leaderNameList = self.db.TeacherSelectAllNameByCollegeId(self.collegeId)  # 获取学院的所有老师列表
        if self.leaderNameList is not False:
            self.input4.Set(self.leaderNameList)
        else:
            self.input4.Clear()

    def OnLeaderChoice(self, event):
        name = event.GetString()
        self.leaderId = self.db.teacherSelectByName(name)

    def OnStatus(self, event):
        self.flag = not self.flag
        if self.flag:  # 新增
            self.button2_1.Hide()  # 隐藏修改
            self.button2_2.Show()  # 打开新增
            self.status.SetLabel("请录入学系")
            self.input1.SetLabel("")
            self.input2.SetLabel("")
            self.input3.SetLabel("")
            self.input4.SetLabel("")
            self.input1.SetEditable(True)
            self.input2.SetEditable(True)
            self.input3.Set(self.collegeNameList)
            self.input4.Clear()
        else:
            self.button2_1.Show()  # 隐藏新增
            self.button2_2.Hide()  # 打开修改
            self.status.SetLabel("请选择学系")
            self.input1.SetLabel("")
            self.input2.SetLabel("")
            self.input3.SetLabel("")
            self.input4.SetLabel("")
            self.input1.SetEditable(False)
            self.input2.SetEditable(False)
            self.input3.Clear()
            self.input4.Clear()

    def OnEdit(self, event):
        global i
        id = self.input1.GetValue()
        name = self.input2.GetValue()
        collegeId = self.collegeId
        leaderId = self.leaderId
        if len(id) == 0:
            self.success("编号不可为空", False)
            return
        if len(name) == 0:
            self.success("学系名不可为空", False)
            return
        # 连接数据库
        if leaderId is "" or leaderId is None:
            i = self.db.departmentUpdate3(id, name, collegeId)
        else:
            i = self.db.departmentUpdate4(id, name, collegeId, leaderId)
        self.db.commit()
        if i > 0:
            self.success("修改成功")
        else:
            self.success("修改失败，请检查", False)

    def OnNew(self, event):
        id = self.input1.GetValue()
        name = self.input2.GetValue()
        collegeId = self.collegeId
        leaderId = self.leaderId
        if len(id) == 0:
            self.success("编号不可为空", False)
            return
        if len(name) == 0:
            self.success("学系名不可为空", False)
            return
        # 连接数据库
        if leaderId is "" or leaderId is None:
            i = self.db.departmentInsert3(id, name, collegeId)
        else:
            i = self.db.departmentInsert4(id, name, collegeId, leaderId)
        self.db.commit()
        if i > 0:
            self.success("新增成功")
        else:
            self.success("新增失败，请检查", False)

    def OnDelete(self, event):
        if self.id is None or self.id is "":
            self.success("请选择学系", False)
        else:
            i = self.db.departmentDelete(self.id)
            self.db.commit()
            if i > 0:
                self.success("删除成功")

    def OnFlash(self, event):
        self.success("窗口刷新中")
        self.input1.SetLabel("")
        self.input2.SetLabel("")
        self.input3.Set(self.collegeNameList)
        self.input4.Clear()
        self.success("刷新完毕", False)

    def success(self, value, flag=True):
        self.status.SetLabel(value)
        if flag:
            self.GetData()
            self.grid.updateData(self.data)
            self.grid.HideCol(2)
            self.grid.HideCol(4)
            self.input1.Clear()
            self.input2.Clear()
            self.input3.Clear()
            self.input4.Clear()
            if self.collegeNameList is not None:
                self.input3.Clear()
                self.input3.Set(self.collegeNameList)
            # 设置控件初始状态
            self.button2_1.Hide()
            self.button2_2.Show()
            self.flag = True  # 初始为新增
            if "刷新" not in value:
                self.status.SetLabel("请录入学系")
