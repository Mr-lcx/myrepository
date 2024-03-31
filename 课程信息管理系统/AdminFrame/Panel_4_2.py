# 教师的课程考核 --- 成绩录入
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
from Database.ReadFile import ReadExcle

class Panel_4_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_4_2')
        # 组织数据
        self.title = ['课程号', '课程名', '学号', '姓名', '学院','班级', '平时成绩','期末成绩','总评成绩']
        self.data = None  # grid数据
        self.ObjectList = []  # 老师自己开课列表
        self.SetFont(self.font10)
        self.GetData() # 获得自己所有学生选课情况

        self.grid = MyGrid(self, self.title, self.data, pos=(50, 50), size=(630, 350), func=self.gridSelect)

        self.staticTextSelect = wx.StaticText(self, label="根据课程号查询：", pos=(40, 14), size=(120, 30))
        self.choice1 = wx.Choice(self, pos=(170, 10), size=(150, 40))
        if self.ObjectList is not None: # 将DetData初始化时 获得的自己所有开课课程号，放入下拉框中
            self.choice1.Set(self.ObjectList)
        self.choice1.SetSelection(0)
        self.choice1.Bind(wx.EVT_CHOICE, self.SearchChoice) # 选择课程号，事件
        self.buttonSearch = wx.Button(self, label="条件筛选", pos=(360, 10), size=(100, 30))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.Search)
        self.buttonSearchAll = wx.Button(self, label="筛选全部", pos=(470, 10), size=(100, 30))
        self.buttonSearchAll.Bind(wx.EVT_BUTTON, self.SearchAll)
        self.buttonImport = wx.Button(self, label="导入成绩文件", pos=(580, 5), size=(160, 40))

        self.buttonImport.Bind(wx.EVT_BUTTON, self.Import)
        self.flag=False # 这个用来标志 是否确定导入成绩

        self.staticTextSelect = wx.StaticText(self, label="等待查询！", pos=(20, 440), size=(150, 30))
        self.staticTextSelect.SetFont(self.font14)

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
        self.data=self.db.GetAllGrade()#  三表操作

    def gridSelect(self,event):
        print("点击单元格！")
        row = event.GetRow() # 获得点击行号

        strtext=" 您选择了 ： "\
            +"\n课程名： "+self.grid.GetCellValue(row, 1)\
                +" 学号： " + self.grid.GetCellValue(row, 2)\
                +" 姓名： " + self.grid.GetCellValue(row, 3)\
                +" 学院： " + self.grid.GetCellValue(row, 4)\
                +" 班级： " + self.grid.GetCellValue(row, 5) \
                + "\n\n 平时成绩： " + self.grid.GetCellValue(row, 6) \
                + " 期末成绩： " + self.grid.GetCellValue(row, 7)\
                + " 总评成绩： " + self.grid.GetCellValue(row, 8)
        self.staticTextSelect.SetLabel(strtext)


    def SearchChoice(self,event):
        selectNum = event.GetString()
        print("选择了",selectNum)


    # 按条件筛选学生选课情况
    def Search(self,event):
        selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        print("筛选++++",selectNum)
        self.data = self.db.GetGradeSelect(selectNum)  # 按条件查询
        self.grid.updateData(self.data)

    # 筛选全部学生选课情况
    def SearchAll(self,event):
        # 获取所有签到纪录
        self.data = self.db.GetAllGrade()  # 三表操作
        self.grid.updateData(self.data)

    # 这里导入Excle文件的成绩单
    def Import(self,event):
        if self.flag:# 正式导入成绩！！！
            self.flag=False
            self.buttonImport.SetLabel("导入成绩文件")
            for item in self.data:
                print(tuple(item))
                fg = self.db.InsertGrade(tuple(item))
                print("****************",fg)
                if fg:
                    self.staticTextSelect.SetLabel("插入成功！")
                    self.data = self.db.GetAllGrade()  # 三表操作
                    self.grid.updateData(self.data)
                else:
                    self.staticTextSelect.SetLabel("插入失败！")
        else:
            fileName=self.onOpenFile()
            readfile=ReadExcle()
            try: # 上传文件需要 符合要求
                self.data=readfile.read(fileName)
                self.flag = True  # True 表示确定录入
                self.buttonImport.SetLabel("确定录入成绩，请点击")
                title = ['学号', '课程号', '平时成绩', '期末成绩', '总评成绩']
                self.grid.updateData1(title, self.data)
            except Exception as e:
                wx.MessageBox("文件类型错误")

    def onOpenFile(self):
        tmp = ""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                tmp=tmp+path
        dlg.Destroy()
        return tmp