
# 教师界面的主窗体

import wx
from Util.MyFrame import MyFrame

from StudentFrame.Panel_1_1 import Panel_1_1  # 学生个人信息管理
from StudentFrame.Panel_1_2 import Panel_1_2  #学生修改密码
from StudentFrame.Panel_2_1 import Panel_2_1 # 学生选课
from StudentFrame.Panel_2_2 import Panel_2_2 # 学生选课情况
from StudentFrame.Panel_3_1 import Panel_3_1 # 学生查看课表
from StudentFrame.Panel_3_2 import Panel_3_2 # 个人签到
from StudentFrame.Panel_4_1 import Panel_4_1 # 学生查看考试安排
from StudentFrame.Panel_4_2 import Panel_4_2 # 学生查看成绩
from StudentFrame.Panel_5_1 import Panel_5_1 # 学生评教
from StudentFrame.Panel_6_2 import Panel_6_2 # 查看公告


class StudentMainFrame(MyFrame):
    def __init__(self,person):
        super().__init__(person=person,title="教务管理系统---学生窗口",
                         size=(800, 600))

        self.panel_1_1 = None  #
        self.panel_1_2 = None  #
        self.panel_1_3 = None
        self.panel_1_4 = None
        self.panel_1_5 = None
        self.panel_2_1 = None
        self.panel_2_2 = None
        self.panel_3_1 = None
        self.panel_3_2 = None
        self.panel_3_3 = None
        self.panel_3_4 = None
        self.panel_4_1 = None
        self.panel_4_2 = None
        self.panel_4_3 = None
        self.panel_5_1 = None
        self.panel_6_1 = None
        self.panel_6_2 = None
        self.hide()

        # 贴主界面图
        img = wx.Image('res/003.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, img, (0, 0))

        self.font16 = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)
        self.SetFont(self.font16)
        self.Center()

        # 创建菜单栏 == 个人信息管理
        menu_1 = wx.Menu()
        menu_1_1 = wx.MenuItem(menu_1, 11, text="个人信息", kind=wx.ITEM_NORMAL)
        menu_1_2 = wx.MenuItem(menu_1, 12, text="修改密码", kind=wx.ITEM_NORMAL)
        menu_1.Append(menu_1_1)
        menu_1.Append(menu_1_2)

        # 创建菜单栏 == 课程管理
        menu_2 = wx.Menu()
        menu_2_1 = wx.MenuItem(menu_1, 21, text="选课系统", kind=wx.ITEM_NORMAL)
        menu_2_2 = wx.MenuItem(menu_1, 22, text="个人选课情况", kind=wx.ITEM_NORMAL)
        menu_2.Append(menu_2_1)
        menu_2.Append(menu_2_2)

        # 创建菜单栏 == 上课安排
        menu_3 = wx.Menu()
        menu_3_1 = wx.MenuItem(menu_3, 31, text="查看课表", kind=wx.ITEM_NORMAL)
        menu_3_2 = wx.MenuItem(menu_3, 32, text="学生签到", kind=wx.ITEM_NORMAL)
        menu_3.Append(menu_3_1)
        menu_3.Append(menu_3_2)

        # 创建菜单栏 == 课程考核
        menu_4 = wx.Menu()
        menu_4_1 = wx.MenuItem(menu_4, 41, text="查看考试时间", kind=wx.ITEM_NORMAL)
        menu_4_2 = wx.MenuItem(menu_4, 42, text="查看成绩", kind=wx.ITEM_NORMAL)
        menu_4.Append(menu_4_1)
        menu_4.Append(menu_4_2)

        # 创建菜单栏 == 评教管理
        menu_5 = wx.Menu()
        menu_5_1 = wx.MenuItem(menu_5, 51, text="查看学生评教", kind=wx.ITEM_NORMAL)
        menu_5.Append(menu_5_1)

        # 创建菜单栏 == 公告
        menu_6 = wx.Menu()
        menu_6_1 = wx.MenuItem(menu_6, 61, text="查看公告", kind=wx.ITEM_NORMAL)
        menu_6.Append(menu_6_1)

        # 系统
        menu_7 = wx.Menu()
        menu_7_1 = wx.MenuItem(menu_7, 71, text="回到首页", kind=wx.ITEM_NORMAL)
        menu_7_2 = wx.MenuItem(menu_7, wx.ID_EXIT, text="退出", kind=wx.ITEM_NORMAL)
        menu_7.Append(menu_7_1)
        menu_7.Append(menu_7_2)

        # 将上面创建的菜单项 加入 到菜刀条里面
        menuBar = wx.MenuBar()
        menuBar.Append(menu_1, '&个人信息管理')
        menuBar.Append(menu_2, '&课程管理')
        menuBar.Append(menu_3, '&上课安排')
        menuBar.Append(menu_4, '&课程考核')
        menuBar.Append(menu_5, '&评教管理')
        menuBar.Append(menu_6, '&公告')
        menuBar.Append(menu_7, '&系统')

        menuBar.SetFont(self.font16)
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.menuhandler)

    def menuhandler(self, event):
        id = event.GetId()
        print(id)
        self.hide()
        self.bitmap.Hide()  # 隐藏图片
        if id == 11:  # 学生个人信息（修改）
            self.panel_1_1 = Panel_1_1(self)
            self.panel_1_1.Show()
            self.SetTitle("学生个人信息---学生窗口")
        if id == 12:  # 修改密码
            self.panel_1_2 = Panel_1_2(self)
            self.panel_1_2.Show()
            self.SetTitle("修改密码---学生窗口")
        if id == 21:  # 学生选课系统
            self.panel_2_1 = Panel_2_1(self)
            self.panel_2_1.Show()
            self.SetTitle("学生选课系统---学生窗口")
        if id == 22:  # 自己选课情况
            self.panel_2_2 = Panel_2_2(self)
            self.panel_2_2.Show()
            self.SetTitle("个人选课情况---学生窗口")
        if id == 31:  # 参看自己课表
            self.panel_3_1 = Panel_3_1(self)
            self.panel_3_1.Show()
            self.SetTitle("查看课表---学生窗口")
        if id == 32:  # 自己课程签到
            self.panel_3_2 = Panel_3_2(self)
            self.panel_3_2.Show()
            self.SetTitle("查看学生签到情况---学生窗口")
        if id == 41:  # 开启考试
            self.panel_4_1 = Panel_4_1(self)
            self.panel_4_1.Show()
            self.SetTitle("开始时间查看---学生窗口")
        if id == 42:  # 教师查看成绩
            self.panel_4_2 = Panel_4_2(self)
            self.panel_4_2.Show()
            self.SetTitle("学生查看成绩---学生窗口")
        if id == 51:  # 查看学生评教
            self.panel_5_1 = Panel_5_1(self)
            self.panel_5_1.Show()
            self.SetTitle("学生评教---学生窗口")

        if id == 61:  # 查看公告
            self.panel_6_2 = Panel_6_2(self)
            self.panel_6_2.Show()
            self.SetTitle("查看公告---学生窗口")

        if id == 71:  # 返回主页
            self.bitmap.Show()
            self.SetTitle("教务管理系统---学生窗口")

        if id == wx.ID_EXIT:# 退出教务系统
            self.Close()

    # 隐藏面板
    def hide(self):
        if self.panel_1_1 is not None:
            self.panel_1_1.Hide()
        if self.panel_1_2 is not None:
            self.panel_1_2.Hide()
        if self.panel_2_1 is not None:
            self.panel_2_1.Hide()
        if self.panel_2_2 is not None:
            self.panel_2_2.Hide()
        if self.panel_3_1 is not None:
            self.panel_3_1.Hide()
        if self.panel_3_2 is not None:
            self.panel_3_2.Hide()
        if self.panel_4_1 is not None:
            self.panel_4_1.Hide()
        if self.panel_4_2 is not None:
            self.panel_4_2.Hide()
        if self.panel_4_3 is not None:
            self.panel_4_3.Hide()
        if self.panel_5_1 is not None:
            self.panel_5_1.Hide()
        if self.panel_6_1 is not None:
            self.panel_6_1.Hide()
        if self.panel_6_2 is not None:
            self.panel_6_2.Hide()