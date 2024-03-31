
# 学生的课程考核 --- 拆查看考试时间
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
import wx.grid

class Panel_4_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_4_1')
        staticText = wx.StaticText(self, pos=(10, 10), size=(300, 32))
        s = "欢迎您：   学号: %s , 姓名: %s ,性别：%s  身份: %s" % (self.person.id, self.person.name, self.person.sex, self.person.type)
        staticText.SetLabel(s)

        # 表头
        self.title=['课程号', '课程名', '任课老师', '考试时间', '考试地点', '考试形式']
        self.data = None  # grid数据
        self.GetAllData()  # 获得开课表的所有纪录
        self.SetFont(self.font10)
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
        self.input6 = wx.TextCtrl(self, pos=(540, 440), size=(150, 20))
        self.status =wx.StaticText(self, label="未选择考试！", pos=(600, 100), size=(130, 40))
        self.status.SetFont(self.font14)

    # 点击单元格 响应：将所点击的行的内容填写到文本框中
    def gridSelect(self,event):
        print("点击单元格")
        # 自动切换修改状态
        self.input1.SetEditable(False)
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        self.input4.SetEditable(False)
        self.input5.SetEditable(False)
        self.input6.SetEditable(False)
        # 获取行号
        row = event.GetRow()
        self.id = self.grid.GetCellValue(row, 0)
        self.status.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        self.input3.SetLabel(self.grid.GetCellValue(row, 2))
        self.input4.SetLabel(self.grid.GetCellValue(row, 3))
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))
        self.input6.SetLabel(self.grid.GetCellValue(row, 5))


    # 查看自己的考试时间
    def GetAllData(self):
        mydata=[]
        objectList=self.GetMyObjectList() # 获得自己所有选课的 课程号
        for item in objectList:
            mydata.append(self.db.GetStudentExam(item))
        self.data=mydata


    # 查看自己的所有选课列表
    def GetMyObjectList(self):
        objectlist = self.db.GetMySc(self.person.id)
        templist = []
        if objectlist is not False:
            for temp in objectlist:
                templist.append(str(temp[0]))
        print(templist)
        return templist