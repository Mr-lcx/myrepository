

import wx

from Util.MyGrid import MyGrid
from Util.MyPanel import MyPanel


class Panel_1_3(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_1_3')
        # 组织数据
        self.title = ['编号', '姓名', '学院', '学系', '手机号']
        self.data = None  # grid数据
        self.teacherId = None  # 当前教师数据
        self.teacherNameList = None  # 教师姓名列表
        self.collegeId = None  # 当前选择学院id
        self.collegeNameList = None  # 学院名列表
        self.departmentId = None  # 学系id
        self.departmentNameList = None  # 学系名列表
        self.departmentNameListChoice = None  # 学系名列表 查询用
        self.id = None  # 当前选择grid
        self.GetData()

        self.SetFont(self.font10)

        self.grid = MyGrid(self, self.title, self.data, pos=(10, 40), size=(530, 450), func=self.gridSelect)

        # 搜索
        self.staticTextSelect = wx.StaticText(self, label="筛选", pos=(10, 14), size=(35, 20))
        self.choice1 = wx.Choice(self, pos=(50, 10), size=(150, 32))
        self.choice2 = wx.Choice(self, pos=(205, 10), size=(150, 32))
        if self.collegeNameList is not None:
            self.choice1.Set(self.collegeNameList)
        self.choice1.Bind(wx.EVT_CHOICE, self.SearchChoice)
        self.buttonSearch = wx.Button(self, label="筛选", pos=(360, 10), size=(70, 20))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.Search)
        self.buttonSearchReset = wx.Button(self, label="还原", pos=(435, 10), size=(70, 20))
        self.buttonSearchReset.Bind(wx.EVT_BUTTON, self.OnFlash)

        self.staticText1 = wx.StaticText(self, label=self.title[0], pos=(550, 40), size=(30, 32))
        self.staticText2 = wx.StaticText(self, label=self.title[1], pos=(550, 80), size=(30, 32))
        self.staticText3 = wx.StaticText(self, label=self.title[2], pos=(550, 120), size=(30, 32))
        self.staticText4 = wx.StaticText(self, label=self.title[3], pos=(550, 160), size=(30, 32))
        self.staticText5 = wx.StaticText(self, label=self.title[4], pos=(550, 200), size=(50, 32))
        self.input1 = wx.TextCtrl(self, pos=(620, 38), size=(150, 20))
        self.input2 = wx.TextCtrl(self, pos=(620, 78), size=(150, 20))
        self.input3 = wx.Choice(self, pos=(620, 118), size=(150, 20))
        self.input4 = wx.Choice(self, pos=(620, 158), size=(150, 20))
        self.input5 = wx.TextCtrl(self, pos=(620, 198), size=(150, 20))
        if self.collegeNameList is not None:
            self.input3.Set(self.collegeNameList)
        if self.departmentNameList is not None:
            self.input4.Set(self.departmentNameList)
        self.input3.Bind(wx.EVT_CHOICE, self.OnCollegeChoice)
        self.input4.Bind(wx.EVT_CHOICE, self.OnDepartmentChoice)
        self.status = wx.StaticText(self, label="当前未选择", pos=(570, 240), size=(130, 32))
        self.button1 = wx.Button(self, label="切换状态", pos=(550, 280), size=(100, 32))
        self.button2_1 = wx.Button(self, label="修改", pos=(660, 280), size=(100, 32))
        self.button2_2 = wx.Button(self, label="新增", pos=(660, 280), size=(100, 32))
        self.flag = True  # 默认为新增状态
        self.button2_1.Hide()
        self.button3 = wx.Button(self, label="删除", pos=(550, 320), size=(100, 32))
        self.button4 = wx.Button(self, label="刷新", pos=(660, 320), size=(100, 32))
        self.button1.Bind(wx.EVT_BUTTON, self.OnStatus)
        self.button2_1.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.button2_2.Bind(wx.EVT_BUTTON, self.OnNew)
        self.button3.Bind(wx.EVT_BUTTON, self.OnDelete)
        self.button4.Bind(wx.EVT_BUTTON, self.OnFlash)
        # 设置控件初始状态
        self.button2_1.Hide()
        self.flag = True  # 初始为新增
        self.status.SetLabel("请录入教师")

    def GetData(self, collegeName=None, departmentName=None):
        teacherListTmp = self.db.teacherSelectAll(collegeName, departmentName)
        teacherList = []
        if teacherListTmp is not False:
            for teacher in teacherListTmp:
                department = self.db.departmentSelectById(teacher[3])
                college = self.db.collegeSelectById(department[2])
                teacherList.append([
                    teacher[0],
                    teacher[1],
                    college[1],
                    department[1],
                    teacher[4]
                ])
        self.data = teacherList
        self.collegeNameList = self.db.collegeSelectAllName()

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
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))
        # 处理input3
        collegeName = self.grid.GetCellValue(row, 2)
        self.collegeId = self.db.collegeSelectIdByName(collegeName)  # 获取学院编号
        self.input3.SetSelection(self.collegeNameList.index(collegeName))
        # 处理input4
        departmentName = self.grid.GetCellValue(row, 3)
        self.departmentId = self.db.departmentSelectIdByName(departmentName)
        self.departmentNameList = self.db.departmentSelectByCollegeId(self.collegeId)  # 从数据库获取学系列表
        self.input4.Set(self.departmentNameList)
        self.input4.SetSelection(self.departmentNameList.index(departmentName))
        event.Skip()

    def SearchChoice(self, event):
        collegeName = event.GetString()
        collegeId = self.db.collegeSelectIdByName(collegeName)
        self.departmentNameListChoice = self.db.departmentSelectByCollegeId(collegeId)
        self.departmentNameListChoice.insert(0, "")
        self.choice2.Clear()
        self.choice2.Set(self.departmentNameListChoice)

    def Search(self, event):
        collegeName = self.choice1.GetString(self.choice1.GetSelection())
        departmentName = self.choice2.GetString(self.choice2.GetSelection())
        self.success("查询成功", collegeName=collegeName, departmentName=departmentName)

    def OnCollegeChoice(self, event):
        name = event.GetString()
        self.collegeId = self.db.collegeSelectIdByName(name)  # 获取学院id
        self.departmentNameList = self.db.departmentSelectByCollegeId(self.collegeId)  # 获取学院下的专业信息列表
        if self.departmentNameList is not False:
            self.input4.Set(self.departmentNameList)
        else:
            self.input4.Clear()

    def OnDepartmentChoice(self, event):
        name = event.GetString()
        self.departmentId = self.db.departmentSelectIdByName(name)

    def OnStatus(self, event):
        self.flag = not self.flag
        if self.flag:  # 新增
            self.button2_1.Hide()  # 隐藏修改
            self.button2_2.Show()  # 打开新增
            self.status.SetLabel("请录入教师")
            self.input1.SetLabel("")
            self.input2.SetLabel("")
            self.input3.SetLabel("")
            self.input4.SetLabel("")
            self.input5.SetLabel("")
            self.input1.SetEditable(True)
            self.input2.SetEditable(True)
            self.input3.Set(self.collegeNameList)
            self.input4.Clear()
        else:
            self.button2_1.Show()  # 隐藏新增
            self.button2_2.Hide()  # 打开修改
            self.status.SetLabel("请选择教师")
            self.input1.SetLabel("")
            self.input2.SetLabel("")
            self.input3.SetLabel("")
            self.input4.SetLabel("")
            self.input5.SetLabel("")
            self.input1.SetEditable(False)
            self.input2.SetEditable(False)
            self.input3.Clear()
            self.input4.Clear()

    def OnEdit(self, event):
        global i
        id = self.input1.GetValue()
        name = self.input2.GetValue()
        departmentId = self.departmentId
        phone = self.input5.GetValue()
        if len(id) == 0:
            self.success("编号不可为空", False)
            return
        if len(name) == 0:
            self.success("姓名不可为空", False)
            return
        if len(departmentId) == 0:
            self.success("请选择学系", False)
            return
        # 连接数据库
        i = self.db.teacherUpdate(id, name, departmentId, phone)
        self.db.commit()
        if i > 0:
            self.success("修改成功")
        else:
            self.success("修改失败，请检查", False)

    def OnNew(self, event):
        id = self.input1.GetValue()
        name = self.input2.GetValue()
        departmentId = self.departmentId
        phone = self.input5.GetValue()
        if len(id) == 0:
            self.success("编号不可为空", False)
            return
        if len(name) == 0:
            self.success("姓名不可为空", False)
            return
        if len(departmentId) == 0:
            self.success("请选择学系", False)
            return
        # 连接数据库
        if phone is "" or phone is None:
            i = self.db.teacherInsert(id, name, departmentId)
        else:
            i = self.db.teacherInsert(id, name, departmentId, phone)
        self.db.commit()
        if i > 0:
            self.success("新增成功")
        else:
            self.success("新增失败，请检查", False)

    def OnDelete(self, event):
        if self.id is None or self.id is "":
            self.success("请选择教师", False)
        else:
            i = self.db.teacherDelete(self.id)
            self.db.commit()
            if i > 0:
                self.success("删除成功")

    def OnFlash(self, event):
        self.success("窗口刷新中")
        self.input1.SetLabel("")
        self.input2.SetLabel("")
        self.input5.SetLabel("")
        self.input3.Set(self.collegeNameList)
        self.input4.Clear()
        self.success("刷新完毕", False)

    def success(self, value, flag=True, collegeName=None, departmentName=None):
        self.status.SetLabel(value)
        if flag:
            self.GetData(collegeName, departmentName)
            self.grid.updateData(self.data)
            self.input1.Clear()
            self.input2.Clear()
            self.input3.Clear()
            self.input4.Clear()
            self.input5.Clear()
            if self.collegeNameList is not None:
                self.input3.Clear()
                self.input3.Set(self.collegeNameList)
            if self.departmentNameList is not None:
                self.input4.Set(self.departmentNameList)
            # 设置控件初始状态
            self.button2_1.Hide()
            self.button2_2.Show()
            self.flag = True  # 初始为新增
            if "刷新" not in value:
                self.status.SetLabel("请录入教师")
