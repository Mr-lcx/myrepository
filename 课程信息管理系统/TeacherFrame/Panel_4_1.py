
# 教师的课程考核 --- 开启考试
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
import wx.grid

class Panel_4_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_4_1')
        # 表头
        self.title=['课程号', '课程名', '任课老师', '考试时间', '考试地点', '考试形式']
        self.Way=['开卷','闭卷']
        self.data = None  # grid数据
        self.GetAllData()  # 获得开课表的所有纪录
        self.SetFont(self.font10)

        self.button_MySc = wx.Button(self, label="查看自己课程考试情况", pos=(180, 10), size=(180, 30))
        self.button_MySc.Bind(wx.EVT_BUTTON, self.ShowMyData)
        self.button_OtherSc = wx.Button(self, label="查看全部老师课程考试情况", pos=(380, 10), size=(180, 30))
        self.button_OtherSc.Bind(wx.EVT_BUTTON, self.ShowAllData)
        # 显示考试情况表格
        self.grid = MyGrid(self, self.title, self.data, pos=(80, 45), size=(450, 320), func=self.gridSelect)
        rowsizeinfo = wx.grid.GridSizesInfo(50, [])  # 固定课表宽和高
        self.grid.SetRowSizes(rowsizeinfo)
        self.staticText1 = wx.StaticText(self, label="课程号", pos=(20, 400), size=(60, 32))
        self.input1 = wx.TextCtrl(self, pos=(80, 400), size=(150, 20))
        self.staticText2 = wx.StaticText(self, label="课程名", pos=(250, 400), size=(60, 32))
        self.input2 = wx.TextCtrl(self, pos=(310, 400), size=(150, 20))
        self.staticText3 = wx.StaticText(self, label="任课老师", pos=(480, 400), size=(60, 32))
        self.input3 = wx.TextCtrl(self, pos=(540, 400), size=(150, 20))

        self.staticText4 = wx.StaticText(self, label="考试时间", pos=(20, 440), size=(60, 32))
        self.input4 = wx.TextCtrl(self, pos=(80, 440), size=(150, 20))
        self.staticText5 = wx.StaticText(self, label="考试地点", pos=(250, 440), size=(60, 32))
        self.input5 = wx.TextCtrl(self, pos=(310, 440), size=(150, 20))
        self.staticText6 = wx.StaticText(self, label="考试形式", pos=(480, 440), size=(60, 32))
        self.input6 = wx.Choice(self, pos=(540, 440), size=(150, 20))
        self.input6.Set(self.Way)

        self.status = wx.StaticText(self, label="当前未选择", pos=(600, 100), size=(130, 40))
        self.button2_1 = wx.Button(self, label="修改", pos=(600, 200), size=(150, 40))
        self.button4 = wx.Button(self, label="刷新", pos=(600, 260), size=(150, 40))
        self.button2_1.Bind(wx.EVT_BUTTON, self.OnEdit)
        self.button4.Bind(wx.EVT_BUTTON, self.OnFlash)
        self.input1.SetEditable(False)
        self.status.SetLabel("请添加考试！")

    # 点击单元格 响应：将所点击的行的内容填写到文本框中
    def gridSelect(self,event):
        print("点击单元格")
        # 自动切换修改状态
        self.input1.SetEditable(False)
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        self.input4.SetEditable(True)
        self.input5.SetEditable(True)
        # 获取行号
        row = event.GetRow()
        self.id = self.grid.GetCellValue(row, 0)
        self.status.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        self.input3.SetLabel(self.grid.GetCellValue(row, 2))
        self.input4.SetLabel(self.grid.GetCellValue(row, 3))
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))

        # 处理input6
        way = self.grid.GetCellValue(row, 5)
        wayId = self.wayIndex(way)  # 获取学院编号
        self.input6.SetSelection(wayId-1)

    # 点击查看所有人的开课纪录
    def ShowAllData(self,event):
        print("获得所有开课数据")
        self.data=self.db.GetAllExam()
        self.grid.updateData(self.data)

    # 点击查看所有人的开课纪录
    def GetAllData(self):
        print("获得所有开课数据")
        self.data=self.db.GetAllExam()

    # 点击显示自己开课纪录
    def ShowMyData(self,event):
        print("获得自己开课数据")
        self.data = self.db.GetMyExam(self.person.name)
        self.grid.updateData(self.data)

    # 编辑开课纪录
    def OnEdit(self, event):
        objectNum = self.input1.GetValue()
        shijian=self.input4.GetValue()
        didian = self.input5.GetValue()
        way = self.input6.GetString(self.input6.GetSelection())

        # 连接数据库
        objectNum=int(objectNum)
        print(objectNum,shijian,didian,way)
        fg = self.db.ExamUpdate(objectNum,shijian,didian,way)
        if fg:
            self.success("添加考试成功")
            self.data = self.db.GetMyExam(self.person.name)
            self.grid.updateData(self.data)
        else:
            self.success("修改失败，请检查", False)



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

    def wayIndex(self,week):
        if week=="开卷":
            return 1
        if week=="闭卷":
            return 2
        return 0
