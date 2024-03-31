# 教师的课程管理 --- 学生签到情况查看
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid

class Panel_3_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_3_2')
        # 组织数据
        self.title = ['课程号', '课程名', '学号', '姓名', '学院','班级', '签到时间','签到次数']
        self.data = None  # grid数据
        self.ObjectList = []  # 老师自己开课列表
        self.SetFont(self.font10)
        self.GetData() # 获得自己所有学生选课情况

        self.grid = MyGrid(self, self.title, self.data, pos=(50, 50), size=(630, 350), func=self.gridSelect)

        self.staticTextSelect = wx.StaticText(self, label="根据课程号查询：", pos=(40, 14), size=(120, 30))
        self.choice1 = wx.Choice(self, pos=(170, 10), size=(150, 40))
        if self.ObjectList is not None: # 将DetData初始化时 获得的自己所有开课课程号，放入下拉框中
            self.choice1.Set(self.ObjectList)
        self.choice1.Bind(wx.EVT_CHOICE, self.SearchChoice) # 选择课程号，事件
        self.buttonSearch = wx.Button(self, label="条件筛选", pos=(360, 10), size=(100, 30))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.Search)
        self.buttonSearchAll = wx.Button(self, label="筛选全部", pos=(470, 10), size=(100, 30))
        self.buttonSearchAll.Bind(wx.EVT_BUTTON, self.SearchAll)

        self.staticTextSelect = wx.StaticText(self, label="等待查询！", pos=(120, 440), size=(150, 30))


    def GetData(self):
        print("初始化课程选择框，以及界面显示所有选课")
        objectlist = self.db.GetMyClassOpen(self.person.name)
        templist=[]
        if objectlist is not False:
            for temp in objectlist:
                templist.append(str(temp[0]))
            self.ObjectList=templist # 将自己开课的课程号全部放入队列
        print(templist)
        # 获取所有签到纪录
        self.data=self.db.GetAllQiandao()#  三表操作

    def gridSelect(self,event):
        print("点击单元格！")
        row = event.GetRow() # 获得点击行号

        strtext=" 您选择了 ： "\
            +"\n课程名： "+self.grid.GetCellValue(row, 1)\
                +" 学号： " + self.grid.GetCellValue(row, 2)\
                +" 姓名： " + self.grid.GetCellValue(row, 3)\
                +" 学院： " + self.grid.GetCellValue(row, 4)\
                +" 班级： " + self.grid.GetCellValue(row, 5) \
                + "\n\n 签到时间： " + self.grid.GetCellValue(row, 6) \
                + " 签到次数： " + self.grid.GetCellValue(row, 7)
        self.staticTextSelect.SetLabel(strtext)


    def SearchChoice(self,event):
        selectNum = event.GetString()
        print("选择了",selectNum)


    # 按条件筛选学生选课情况
    def Search(self,event):
        selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        print("筛选++++",selectNum)
        self.data = self.db.GetQiandaoSelect(selectNum)  # 按条件查询
        self.grid.updateData(self.data)

    # 筛选全部学生选课情况
    def SearchAll(self,event):
        # 获取所有签到纪录
        self.data = self.db.GetAllQiandao()  # 三表操作
        self.grid.updateData(self.data)