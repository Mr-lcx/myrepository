# 教师的上课安排 --- 查看课表
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
import wx.grid

class Panel_3_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_3_1')
        self.tableText = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        self.data = [["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]]
        self.GetTableData() # 初始化上课表
        # 提示信息：
        self.staticMy = wx.StaticText(self, label="", pos=(20, 20), size=(130, 40))
        self.staticMy.SetLabel("欢迎你参看课表："+self.person.name)
        self.grid = MyGrid(self, self.tableText, self.data, pos=(10, 50), size=(800, 350), func=self.gridSelect)
        rowsizeinfo = wx.grid.GridSizesInfo(60, []) # 固定课表宽和高
        self.grid.SetRowSizes(rowsizeinfo)
        self.staticText = wx.StaticText(self, label="课程安排：", pos=(20, 440), size=(130, 40))
        self.staticTextSelect = wx.StaticText(self, label="", pos=(160, 440), size=(35, 20))
        self.staticTextSelect.SetFont(self.font16)

    # 点击单元格，将需选择的内容显示出来
    def gridSelect(self,event):
        row = event.GetRow()
        col=event.GetCol()
        self.grid.GetCellValue(row, col)
        self.staticTextSelect.SetLabel(self.grid.GetCellValue(row, col))

    # 获得课程表，从数据库中获取星期几，第几节，让后排版
    def GetTableData(self):
        data=self.db.GetMySc(self.person.id)
        for item in data:
            strdata = " 课程：" + item[1] + "\n 上课地点：" + item[7]
            col=self.GetCol(item[5])
            row=self.GetRow(item[6])
            self.data[col][row]=strdata

    def GetRow(self,num):
        if num=="第一大节":
            return 1
        if num=="第二大节":
            return 2
        if num=="第三大节":
            return 3
        if num=="第四大节":
            return 4

    def GetCol(self,num):
        if num=="星期一":
            return 1
        if num=="星期二":
            return 2
        if num=="星期三":
            return 3
        if num=="星期四":
            return 4
        if num=="星期五":
            return 5
