
import wx

from AdminFrame.Panel_1_1 import Panel_1_1
from AdminFrame.Panel_1_2 import Panel_1_2
from AdminFrame.Panel_1_3 import Panel_1_3
from AdminFrame.Panel_1_4 import Panel_1_4
from AdminFrame.Panel_1_5 import Panel_1_5
from AdminFrame.Panel_2_1 import Panel_2_1
from AdminFrame.Panel_2_2 import Panel_2_2
from AdminFrame.Panel_3_1 import Panel_3_1
from AdminFrame.Panel_3_2 import Panel_3_2
from AdminFrame.Panel_4_1 import Panel_4_1
from AdminFrame.Panel_4_2 import Panel_4_2
from AdminFrame.Panel_4_3 import Panel_4_3
from AdminFrame.Panel_5_1 import Panel_5_1
from AdminFrame.Panel_5_2 import Panel_5_2
from Util.MyFrame import MyFrame


class AdminMainFrame(MyFrame):
    def __init__(self, person):
        super().__init__(person=person,
                         title="教务管理系统---管理员窗口",
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
        self.panel_5_2 = None
        self.hide()

        img = wx.Image('res/002.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, img, (0, 0))
        # self.bitmap.Hide()  # 测试时打开

        # 教务信息管理
        menu_1 = wx.Menu()
        menu_1_1 = wx.MenuItem(menu_1, 11, text="学院信息管理", kind=wx.ITEM_NORMAL)
        menu_1_2 = wx.MenuItem(menu_1, 12, text="学系信息管理", kind=wx.ITEM_NORMAL)
        menu_1_3 = wx.MenuItem(menu_1, 13, text="教师信息管理", kind=wx.ITEM_NORMAL)
        menu_1_4 = wx.MenuItem(menu_1, 14, text="班级信息管理", kind=wx.ITEM_NORMAL)
        menu_1_5 = wx.MenuItem(menu_1, 15, text="学生信息管理", kind=wx.ITEM_NORMAL)
        if person.type is 'admin':
            menu_1.Append(menu_1_1)
            menu_1.Append(menu_1_2)
            menu_1.Append(menu_1_3)
            menu_1.Append(menu_1_4)
            menu_1.Append(menu_1_5)
        elif person.type is 'teacher':
            menu_1.Append(menu_1_4)
            menu_1.Append(menu_1_5)
        elif person.type is 'student':
            pass
        # 个人信息管理
        menu_2 = wx.Menu()
        menu_2_1 = wx.MenuItem(menu_1, 21, text="修改资料", kind=wx.ITEM_NORMAL)
        menu_2_2 = wx.MenuItem(menu_1, 22, text="修改密码", kind=wx.ITEM_NORMAL)
        menu_2.Append(menu_2_1)
        menu_2.Append(menu_2_2)
        # 课程信息管理
        menu_3 = wx.Menu()
        menu_3_1 = wx.MenuItem(menu_3, 31, text="开课管理", kind=wx.ITEM_NORMAL)
        menu_3_2 = wx.MenuItem(menu_3, 32, text="选课情况", kind=wx.ITEM_NORMAL)
        if person.type is 'admin':
            menu_3.Append(menu_3_1)
            menu_3.Append(menu_3_2)

        # 成绩管理
        menu_4 = wx.Menu()
        menu_4_1 = wx.MenuItem(menu_4, 41, text="开启考试", kind=wx.ITEM_NORMAL)
        menu_4_2 = wx.MenuItem(menu_4, 42, text="成绩录入", kind=wx.ITEM_NORMAL)
        menu_4_3 = wx.MenuItem(menu_4, 43, text="查看成绩", kind=wx.ITEM_NORMAL)
        if person.type is 'admin':
            menu_4.Append(menu_4_1)
            menu_4.Append(menu_4_2)
            menu_4.AppendSeparator()
            menu_4.Append(menu_4_3)

        # 公告
        menu_5 = wx.Menu()
        menu_5_1 = wx.MenuItem(menu_5, 51, text="查看公告", kind=wx.ITEM_NORMAL)
        menu_5_2 = wx.MenuItem(menu_5, 52, text="发布公告", kind=wx.ITEM_NORMAL)
        if person.type is 'admin':
            menu_5.Append(menu_5_1)
            menu_5.Append(menu_5_2)

        # 系统
        menu_6 = wx.Menu()
        menu_6_1 = wx.MenuItem(menu_6, 61, text="回到首页", kind=wx.ITEM_NORMAL)
        menu_6_2 = wx.MenuItem(menu_6, wx.ID_EXIT, text="退出", kind=wx.ITEM_NORMAL)
        menu_6.Append(menu_6_1)
        menu_6.Append(menu_6_2)

        menuBar = wx.MenuBar()
        if person.type is 'admin':
            menuBar.Append(menu_1, '&教务信息管理')
            menuBar.Append(menu_2, '&个人信息管理')
            menuBar.Append(menu_3, '&课程信息管理')
            menuBar.Append(menu_4, '&成绩管理')
            menuBar.Append(menu_5, '&公告')
            menuBar.Append(menu_6, '&系统')

        menuBar.SetFont(self.font16)
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.menuhandler)

    def hide(self):
        if self.panel_1_1 is not None:
            self.panel_1_1.Hide()
        if self.panel_1_2 is not None:
            self.panel_1_2.Hide()
        if self.panel_1_3 is not None:
            self.panel_1_3.Hide()
        if self.panel_1_4 is not None:
            self.panel_1_4.Hide()
        if self.panel_1_5 is not None:
            self.panel_1_5.Hide()
        if self.panel_2_1 is not None:
            self.panel_2_1.Hide()
        if self.panel_2_2 is not None:
            self.panel_2_2.Hide()
        if self.panel_3_1 is not None:
            self.panel_3_1.Hide()
        if self.panel_3_2 is not None:
            self.panel_3_2.Hide()
        if self.panel_3_3 is not None:
            self.panel_3_3.Hide()
        if self.panel_3_4 is not None:
            self.panel_3_4.Hide()
        if self.panel_4_1 is not None:
            self.panel_4_1.Hide()
        if self.panel_4_2 is not None:
            self.panel_4_2.Hide()
        if self.panel_4_3 is not None:
            self.panel_4_3.Hide()
        if self.panel_5_1 is not None:
            self.panel_5_1.Hide()
        if self.panel_5_2 is not None:
            self.panel_5_2.Hide()

    def menuhandler(self, event):
        id = event.GetId()
        print(id)
        self.bitmap.Hide()
        self.hide()
        if id == 11:  # 学院信息管理
            self.panel_1_1 = Panel_1_1(self)
            self.panel_1_1.Show()
            self.SetTitle("学院信息管理---管理员窗口")
        if id == 12:  # 学系信息管理
            self.panel_1_2 = Panel_1_2(self)
            self.panel_1_2.Show()
            self.SetTitle("学系信息管理---管理员窗口")
        if id == 13:  # 教师信息管理
            self.panel_1_3 = Panel_1_3(self)
            self.panel_1_3.Show()
            self.SetTitle("教师信息管理---管理员窗口")
        if id == 14:  # 班级信息管理
            self.panel_1_4 = Panel_1_4(self)
            self.panel_1_4.Show()
            self.SetTitle("班级信息管理---管理员窗口")
        if id == 15:  # 学生信息管理
            self.panel_1_5 = Panel_1_5(self)
            self.panel_1_5.Show()
            self.SetTitle("学生信息管理---管理员窗口")
        if id == 21:  # 修改资料
            self.panel_2_1 = Panel_2_1(self)
            self.panel_2_1.Show()
            self.SetTitle("修改资料---管理员窗口")
        if id == 22:  # 修改密码
            self.panel_2_2 = Panel_2_2(self)
            self.panel_2_2.Show()
            self.SetTitle("修改密码---管理员窗口")
        if id == 31:  # 开课管理
            self.panel_3_1 = Panel_3_1(self)
            self.panel_3_1.Show()
            self.SetTitle("开课管理---管理员窗口")
        if id == 32:  # 选课管理
            if self.panel_3_2 is None:
                self.panel_3_2 = Panel_3_2(self)
            self.panel_3_2.Show()
            self.SetTitle("开课管理---管理员窗口")
        if id == 41:  # 开启考试
            self.panel_4_1 = Panel_4_1(self)
            self.panel_4_1.Show()
            self.SetTitle("开启考试---管理员窗口")
        if id == 42:  # 成绩录入情况
            if self.panel_4_2 is None:
                self.panel_4_2 = Panel_4_2(self)
            self.panel_4_2.Show()
            self.SetTitle("成绩录入情况---管理员窗口")
        if id == 43:  # 查看成绩
            self.panel_4_3 = Panel_4_3(self)
            self.panel_4_3.Show()
            self.SetTitle("查看成绩---管理员窗口")
        if id == 51:  # 查看公告
            self.panel_5_1 = Panel_5_1(self)
            self.panel_5_1.Show()
            self.SetTitle("查看公告---管理员窗口")
        if id == 52:  # 发布公告
            if self.panel_5_2 is None:
                self.panel_5_2 = Panel_5_2(self)
            self.panel_5_2.Show()
            self.SetTitle("发布公告---管理员窗口")
        if id == 61:  # 回到首页
            self.bitmap.Show()
            self.SetTitle("教务管理系统---管理员窗口")
        if id == wx.ID_EXIT:
            self.Close()
