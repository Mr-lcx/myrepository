# 教师的课程管理 --- 开课情况查看
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid

class Panel_2_2(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_2_2')
        # 表头
        self.title = ['课程号', '课程名', '任课老师', '学分', '学时', '星期几',
                      '第几节', '教室', '平时成绩占比', '期末成绩占比', '评教']
        self.data = self.db.GetMySc(self.person.id)
        self.SetFont(self.font10)
        # 显示开课情况表格
        self.grid = MyGrid(self, self.title, self.data, pos=(10, 40), size=(650, 350), func=self.gridSelect)
        self.grid.updateData(self.data)
        self.staticText1 = wx.StaticText(self, label="课程号", pos=(20, 400), size=(60, 32))
        self.input1 = wx.TextCtrl(self, pos=(80, 400), size=(150, 20))
        self.staticText2 = wx.StaticText(self, label="课程名", pos=(250, 400), size=(60, 32))
        self.input2 = wx.TextCtrl(self, pos=(310, 400), size=(150, 20))
        self.staticText3 = wx.StaticText(self, label="老师", pos=(480, 400), size=(60, 32))
        self.input3 = wx.TextCtrl(self, pos=(540, 400), size=(150, 20))

        self.staticText4 = wx.StaticText(self, label="学分", pos=(20, 440), size=(60, 32))
        self.input4 = wx.TextCtrl(self, pos=(80, 440), size=(150, 20))
        self.staticText5 = wx.StaticText(self, label="学时", pos=(250, 440), size=(60, 32))
        self.input5 = wx.TextCtrl(self, pos=(310, 440), size=(150, 20))
        self.staticText6 = wx.StaticText(self, label="教室", pos=(480, 440), size=(60, 32))
        self.input6 = wx.TextCtrl(self, pos=(540, 440), size=(150, 20))

        self.staticText7 = wx.StaticText(self, label="星期几", pos=(20, 480), size=(60, 32))
        self.input7 = wx.TextCtrl(self, pos=(80, 480), size=(150, 20))
        self.staticText8 = wx.StaticText(self, label="第几节", pos=(250, 480), size=(60, 32))
        self.input8 = wx.TextCtrl(self, pos=(310, 480), size=(150, 20))
        self.staticText9 = wx.StaticText(self, label="期末占比", pos=(480, 480), size=(60, 32))
        self.input9 = wx.TextCtrl(self, pos=(540, 480), size=(150, 20))

        self.status = wx.StaticText(self, label="当前未选择", pos=(670, 100), size=(130, 32))
        # 设置控件初始状态
        self.status.SetLabel("点击可查看详情！")

        # 点击单元格 响应：将所点击的行的内容填写到文本框中
    def gridSelect(self, event):
        print("点击单元格")
        self.input1.SetEditable(False)
        self.input2.SetEditable(False)
        self.input3.SetEditable(False)
        self.input4.SetEditable(False)
        self.input5.SetEditable(False)
        self.input6.SetEditable(False)
        self.input7.SetEditable(False)
        self.input8.SetEditable(False)
        self.input9.SetEditable(False)
        # 获取行号
        row = event.GetRow()
        self.id = self.grid.GetCellValue(row, 0)
        self.status.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        self.input3.SetLabel(self.grid.GetCellValue(row, 2))
        self.input4.SetLabel(self.grid.GetCellValue(row, 3))
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))
        self.input6.SetLabel(self.grid.GetCellValue(row, 7))
        self.input7.SetLabel(self.grid.GetCellValue(row, 5))
        self.input8.SetLabel(self.grid.GetCellValue(row, 8))
        self.input9.SetLabel(self.grid.GetCellValue(row, 9))

