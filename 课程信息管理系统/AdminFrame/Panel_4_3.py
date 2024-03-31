# 教师的课程考核 --- 成绩录入
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
from Database.ReadFile import ReadExcle

class Panel_4_3(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_4_3')
        # 组织数据
        self.title = ['学号', '课程号', '平时成绩','期末成绩','总评成绩']
        self.data = None  # grid数据
        self.ObjectList = []  # 老师自己开课列表
        self.SetFont(self.font10)
        self.GetData() # 获得自己所有学生选课情况

        self.grid = MyGrid(self, self.title, self.data, pos=(140, 50), size=(430, 350), func=self.gridSelect)

        self.staticTextSelect = wx.StaticText(self, label="根据课程号查询：", pos=(40, 14), size=(120, 30))
        self.choice1 = wx.Choice(self, pos=(170, 10), size=(150, 40))
        if self.ObjectList is not None: # 将DetData初始化时 获得的自己所有开课课程号，放入下拉框中
            self.choice1.Set(self.ObjectList)
        self.choice1.SetSelection(0)
        self.choice1.Bind(wx.EVT_CHOICE, self.SearchChoice) # 选择课程号，事件
        self.buttonSearch = wx.Button(self, label="条件筛选", pos=(360, 10), size=(100, 30))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.Search)
        self.buttonSearchAll = wx.Button(self, label="查询全校成绩", pos=(470, 10), size=(100, 30))
        self.buttonSearchAll.Bind(wx.EVT_BUTTON, self.SearchAll)
        self.staticText = wx.StaticText(self, label="本界面可查全校\n    所有成绩！", pos=(580, 20), size=(150, 30))
        self.staticText.SetFont(self.font14)
        self.staticTextSelect = wx.StaticText(self, label="等待查询！", pos=(20, 440), size=(150, 30))
        self.staticTextSelect.SetFont(self.font14)

    def GetData(self):
        print("初始化课程选择框，以及界面显示所有选课")
        objectlist = self.db.GetAllClassOfGrade()
        templist=[]
        if objectlist is not False:
            for temp in objectlist:
                templist.append(str(temp[0]))
            self.ObjectList=templist # 将自己开课的课程号全部放入队列
        print(templist)
        # 获取全校所有的课程的全部成绩
        self.data=self.db.GetSchoolAllGrade()

    # 点击单元格
    def gridSelect(self,event):
        print("点击单元格！")
        row = event.GetRow() # 获得点击行号
        strtext=" 您选择了 ： "\
                +" 学号： " + self.grid.GetCellValue(row, 0)\
                +" 课程号： " + self.grid.GetCellValue(row, 1)\
                + "\n\n 平时成绩： " + self.grid.GetCellValue(row, 2) \
                + " 期末成绩： " + self.grid.GetCellValue(row, 3)\
                + " 总评成绩： " + self.grid.GetCellValue(row, 4)
        self.staticTextSelect.SetLabel(strtext)


    def SearchChoice(self,event):
        selectNum = event.GetString()
        print("选择了",selectNum)


    # 按条件筛选学生选课情况
    def Search(self,event):
        selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        print("筛选++++",selectNum)
        self.data = self.db.GetSchoolGradeSelect(selectNum)  # 按条件查询
        self.grid.updateData(self.data)

    # 筛选全部学生选课情况
    def SearchAll(self,event):
        # 获取全校所有的课程的全部成绩
        self.data = self.db.GetSchoolAllGrade()
        self.grid.updateData(self.data)