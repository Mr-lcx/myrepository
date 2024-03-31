# 学生的课程考核 --- 成绩查看
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
from Database.ReadFile import ReadExcle

class Panel_4_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_4_2')
        staticText = wx.StaticText(self, label="**************** 欢迎查看个人成绩 ****************",pos=(100, 10), size=(800, 32))
        # 组织数据
        self.title = ['课程号', '课程名', '学号', '姓名', '学院','班级', '平时成绩','期末成绩','总评成绩']
        self.data = None  # grid数据
        self.SetFont(self.font10)
        self.GetData() # 获得自己所有学生选课情况

        self.grid = MyGrid(self, self.title, self.data, pos=(50, 50), size=(630, 350), func=self.gridSelect)
        self.staticTextSelect = wx.StaticText(self, label="等待！！！", pos=(20, 440), size=(150, 30))
        self.staticTextSelect.SetFont(self.font14)

    def GetData(self):
        self.data=self.db.GetMyAllGrade(self.person.id)#  三表操作

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

