# 教师的课程考核 --- 成绩录入
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
import wx.grid

class Panel_5_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_5_1')
        # 组织数据
        self.title = ['课程号', '课程名', '任课老师', '学分', '学时', '学生等级评教(数字越大评价越好！)']
        self.data = None  # grid数据
        self.SetFont(self.font10)
        self.GetData() # 获得自己所有学生选课情况

        self.grid = MyGrid(self, self.title, self.data, pos=(140, 50), size=(530, 330), func=self.gridSelect)
        rowsizeinfo = wx.grid.GridSizesInfo(40, [])  # 固定课表宽和高
        self.grid.SetRowSizes(rowsizeinfo)
        self.staticText = wx.StaticText(self, label="***** 全校教师评教情况 *****", pos=(250, 10), size=(150, 30))
        self.staticText.SetFont(self.font14)

        self.staticTextSelect = wx.StaticText(self, label="查看评教信息~", pos=(20, 420), size=(200, 30))
        self.staticTextSelect.SetFont(self.font14)

    def GetData(self):
        # 获取全校所有的课程的全部成绩
        self.data=self.db.GetTeacherComment()

    # 点击单元格
    def gridSelect(self,event):
        print("点击单元格！")
        row = event.GetRow() # 获得点击行号
        strtext=" 您选择了 ： "\
                +"  课程号： " + self.grid.GetCellValue(row, 0)\
                +"  课程名： " + self.grid.GetCellValue(row, 1)\
                + "  任课老师： " + self.grid.GetCellValue(row, 2) \
                + "\n\n 学分： " + self.grid.GetCellValue(row, 3)\
                + "  学时： " + self.grid.GetCellValue(row, 4) \
                + "  评教等级： " + self.grid.GetCellValue(row, 5)
        self.staticTextSelect.SetLabel(strtext)