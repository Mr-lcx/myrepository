# 教师的课程考核 --- 成绩录入
import wx
from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid
import wx.grid

class Panel_5_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_5_1')
        self.title = ['课程号', '课程名', '任课老师', '学分', '学时', '星期几',
                      '第几节', '教室', '平时成绩占比', '期末成绩占比', '评教']
        self.data = None
        self.ObjectList = []  # 老师自己选课列表

        self.Count=0
        self.SetFont(self.font10)
        self.GetData() # 初始化数据
        # 显示开课情况表格
        self.grid = MyGrid(self, self.title, self.data, pos=(10, 60), size=(680, 330), func=self.gridSelect)

        self.staticTextSelect = wx.StaticText(self, label="根据课程号查询：", pos=(40, 14), size=(120, 30))
        self.choice1 = wx.Choice(self, pos=(160, 10), size=(130, 40))
        if self.ObjectList is not None:  # 将DetData初始化时 获得的自己所有开课课程号，放入下拉框中
            self.choice1.Set(self.ObjectList)
        self.buttonSearch = wx.Button(self, label="条件筛选", pos=(320, 10), size=(100, 30))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.Search)
        self.buttonSearchAll = wx.Button(self, label="筛选全部", pos=(430, 10), size=(100, 30))
        self.buttonSearchAll.Bind(wx.EVT_BUTTON, self.SearchAll)
        self.buttonGood = wx.Button(self, label="好评", pos=(540, 10), size=(100, 30))
        self.buttonGood.Bind(wx.EVT_BUTTON, self.Good)
        self.buttonBad = wx.Button(self, label="差评", pos=(650, 10), size=(100, 30))
        self.buttonBad.Bind(wx.EVT_BUTTON, self.Bad)

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


    # 获得初始化数据
    def GetData(self):
        print("初始化课程选择框，以及界面显示所有选课")
        objectlist = self.db.GetMySc(self.person.id)
        templist=[]
        if objectlist is not False:
            for temp in objectlist:
                templist.append(str(temp[0]))
            self.ObjectList=templist # 将自己开课的课程号全部放入队列
        print(templist)
        # 获取所有签到纪录
        self.data=self.db.GetMySc(self.person.id) # 获得自己的选课

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
        self.input1.SetLabel(self.grid.GetCellValue(row, 0))
        self.selectNum=int(self.grid.GetCellValue(row, 0)) # 设置评教课程
        self.input2.SetLabel(self.grid.GetCellValue(row, 1))
        self.input3.SetLabel(self.grid.GetCellValue(row, 2))
        self.input4.SetLabel(self.grid.GetCellValue(row, 3))
        self.input5.SetLabel(self.grid.GetCellValue(row, 4))
        self.input6.SetLabel(self.grid.GetCellValue(row, 7))
        self.input7.SetLabel(self.grid.GetCellValue(row, 5))
        self.input8.SetLabel(self.grid.GetCellValue(row, 8))
        self.input9.SetLabel(self.grid.GetCellValue(row, 9))
        self.Count=int(self.grid.GetCellValue(row, 10)) # 获得点击行的评价等级
        # 按条件筛选学生签到情况

    def Search(self, event):
        self.selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        self.data = self.db.GetMySearchSc(self.person.id,self.selectNum)  # 获得自己的选课
        self.grid.updateData(self.data)
        self.Count=int(self.data[0][10]) # 按条件筛选 获得评价等级

    # 筛选自己所有签到情况
    def SearchAll(self, event):
        self.data = self.db.GetMySc(self.person.id)  # 获得自己的选课
        self.grid.updateData(self.data)

    # 好评
    def Good(self, event):
        print("好评！！！")
        self.selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        print("好评结果：",self.selectNum, self.Count)
        fg = self.db.GoodorBadInsert(self.selectNum,self.Count+1)  # 插入好评 评价等级 +1
        if fg:
            wx.MessageBox("好评成功！！！")
            self.data = self.db.GetMySc(self.person.id)  # 三表操作
            self.grid.updateData(self.data)
        else:
            wx.MessageBox("好评失败！！！")

    # 差评
    def Bad(self, event):
        print("差评！！！")
        self.selectNum = int(self.choice1.GetString(self.choice1.GetSelection()))
        fg = self.db.GoodorBadInsert(self.selectNum, self.Count - 1)  # 插入好评 评价等级 +1
        if fg:
            wx.MessageBox("差评成功！！！")
            self.data = self.db.GetMySc(self.person.id)  # 三表操作
            self.grid.updateData(self.data)
        else:
            wx.MessageBox("差评失败！！！")