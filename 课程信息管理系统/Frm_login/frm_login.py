"""
    登录界面，根据redio选择的身份不同，进入不同的页面
"""
import wx

from TeacherFrame.TeacherMainFrame import TeacherMainFrame  # 引入教师的主窗体
from StudentFrame.StudentMainFrame import StudentMainFrame  # 引入学生的主窗体
from AdminFrame.AdminMainFrame import AdminMainFrame
from Entity.Student import Student
from Entity.Teacher import Teacher
from Entity.Admin import Admin
from Util.MyFrame import MyFrame
from Frm_login.Register import Register


class LoginFrame(MyFrame):
    def __init__(self):
        super().__init__(title="登录",
                         size=(350, 300))
        font11 = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        panel = wx.Panel(self)
        # 用户名
        staticName = wx.StaticText(panel, label='请输入用户名:')
        self.textName = wx.TextCtrl(panel, value="1001")
        self.textName.SetFont(font11)
        # 密码
        staticPassword = wx.StaticText(panel, label='  请输入密码:')
        self.textPassword = wx.TextCtrl(panel, value="123456", style=wx.TE_PASSWORD)
        self.textPassword.SetFont(font11)
        # 身份
        self.radioButtonAdmin = wx.RadioButton(panel, label='管理员', style=wx.RB_GROUP)
        self.radioButtonTeacher = wx.RadioButton(panel, label='教师')
        self.radioButtonStudent = wx.RadioButton(panel, label='学生')
        self.radioButtonAdmin.SetValue(True)
        # self.radioButtonTeacher.SetValue(True)
        self.radioButtonAdmin.Bind(wx.EVT_RADIOBUTTON, self.RBadmin)
        self.radioButtonTeacher.Bind(wx.EVT_RADIOBUTTON, self.RBteacher)
        self.radioButtonStudent.Bind(wx.EVT_RADIOBUTTON, self.RBstudent)
        # 按钮
        buttonOK = wx.Button(panel, label="登录")
        buttonOK.Bind(wx.EVT_BUTTON, self.OnOk)
        buttonRegister = wx.Button(panel, label="注册")
        buttonRegister.Bind(wx.EVT_BUTTON, self.OnRegister)
        # 用户名横向布局
        boxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer1.Add(staticName, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer1.Add(self.textName, 1)
        # 密码横向布局
        boxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer2.Add(staticPassword, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, border=10)
        boxSizer2.Add(self.textPassword, 1)
        # 身份横向布局
        boxSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer3.Add(self.radioButtonAdmin, 1)
        boxSizer3.Add(self.radioButtonTeacher, 1)
        boxSizer3.Add(self.radioButtonStudent, 1)
        boxSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer4.Add(buttonOK, 1)
        boxSizer4.Add(buttonRegister, 1)
        # 窗口纵向布局
        mainBoxSizer = wx.BoxSizer(wx.VERTICAL)
        mainBoxSizer.Add(boxSizer1, 1, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        mainBoxSizer.Add(boxSizer2, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer3, 1, flag=wx.ALIGN_CENTER)
        mainBoxSizer.Add(boxSizer4, 1, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)
        panel.SetSizer(mainBoxSizer)

    def OnOk(self, event):
        id = self.textName.GetValue()
        password = self.textPassword.GetValue()
        flag = self.radioButtonAdmin.GetValue()  # 获得哪个单选按钮被选择了
        flag1 = self.radioButtonStudent.GetValue()
        flag2 = self.radioButtonTeacher.GetValue()

        # 下面对登录信息进行验证
        if flag1 and self.db.loginStudent(id, password):  # 学生登录
            print('login student')
            tmp = self.db.loginStudent(id, password)
            student = Student(tmp[0], tmp[1], tmp[2], tmp[5], tmp[6])
            self.StudentloginSuccess(student)

        if flag2 and self.db.loginTeacher(id, password):  # 教师登录
            print('login teacher')
            tmp = self.db.loginTeacher(id, password)
            teacher = Teacher(tmp[0], tmp[1], tmp[2], tmp[5], tmp[6])
            self.TeacherloginSuccess(teacher)

        if flag and self.db.loginAdmin(id, password):
            print('login admin')
            tmp = self.db.adminSelectById(id)
            admin = Admin(tmp[0], tmp[1])
            self.AdminloginSuccess(admin)

    # 教师登录成功
    def TeacherloginSuccess(self, person):
        mainFrame = TeacherMainFrame(person)
        mainFrame.Show()
        self.Close()

    # 学生登录成功
    def StudentloginSuccess(self, person):
        mainFrame = StudentMainFrame(person)
        mainFrame.Show()
        self.Close()

    # 管理员登录成功
    def AdminloginSuccess(self, person):
        mainFrame = AdminMainFrame(person)
        mainFrame.Show()
        self.Close()

    # 单选管理员--设置初值
    def RBadmin(self, event):
        self.textName.SetValue("1001")

    # 单选教师--设置初值
    def RBteacher(self, event):
        self.textName.SetValue("1001")

    # 单选学生--设置初值
    def RBstudent(self, event):
        self.textName.SetValue("18211510124")

    # 注册
    def OnRegister(self, event):
        flag1 = self.radioButtonStudent.GetValue()
        flag2 = self.radioButtonTeacher.GetValue()
        if flag1:
            print("注册学生账号！")
            frame = Register("student")
            frame.Show()
        if flag2:
            print("注册教师账号！")
            frame = Register("teacher")
            frame.Show()
