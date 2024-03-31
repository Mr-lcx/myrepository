

import wx

from Util.MyPanel import MyPanel
from Util.MyGrid import MyGrid


class Panel_1_1(MyPanel):
    def __init__(self, parent):
        super().__init__(parent, 'Panel_1_1')
        self.data = self.db.collegeSelectAll()
        self.title = ['编号', '名称']

        self.grid = MyGrid(self, self.title, self.data, pos=(10, 10), size=(375, 500), func=self.gridSelect)

        # 修改
        self.staticText1 = wx.StaticText(self, label="当前未选择", pos=(450, 40))
        self.textReName = wx.TextCtrl(self, size=(300, 32), pos=(450, 80))
        buttonReName = wx.Button(self, label="修改", size=(300, 40), pos=(450, 120))
        buttonReName.Bind(wx.EVT_BUTTON, self.OnRename)
        # 设置修改控件初始状态
        if len(self.data) > 0:
            self.gridSelectId = self.data[0][0]  # 存放grid的选择值
            self.staticText1.SetLabel("选择了" + self.data[0][1])
            self.textReName.SetLabel(self.data[0][1])
        else:
            self.gridSelectId = None
            self.textReName.SetEditable(False)

        # 新增
        staticText2 = wx.StaticText(self, label="请输入新增学院名", size=(300, 32), pos=(450, 175))
        staticText3 = wx.StaticText(self, label="请输入新增的编号", size=(300, 32), pos=(450, 255))
        self.textNewName = wx.TextCtrl(self, size=(300, 32), pos=(450, 210))
        self.textNewId = wx.TextCtrl(self, size=(300, 32), pos=(450, 290))
        buttonNew = wx.Button(self, label="新增", size=(300, 40), pos=(450, 330))
        buttonNew.Bind(wx.EVT_BUTTON, self.OnNew)
        # 删除
        buttondelete = wx.Button(self, label="删除", size=(300, 40), pos=(450, 395))
        buttondelete.Bind(wx.EVT_BUTTON, self.OnDelete)
        # 刷新
        buttonFlash = wx.Button(self, label="刷新", size=(300, 40), pos=(450, 460))
        buttonFlash.Bind(wx.EVT_BUTTON, self.OnFlash)

    def gridSelect(self, event):
        row = event.GetRow()
        self.gridSelectId = self.grid.GetCellValue(row, 0)
        self.staticText1.SetLabel("选择了" + self.grid.GetCellValue(row, 1))
        self.textReName.SetLabel(self.grid.GetCellValue(row, 1))
        self.textReName.SetEditable(True)
        event.Skip()

    def OnRename(self, event):
        id = self.gridSelectId
        name = self.textReName.GetValue()
        if len(name) > 0:
            # TODO: 'DBManager' object has no attribute 'collegeUpdate'
            i = self.db.collegeUpdate(id, name)
            self.db.commit()
            if i > 0:
                self.success("修改成功")
            return
        else:
            self.success("学院名不可为空", True)

    def OnNew(self, event):
        id = self.textNewId.GetValue()
        name = self.textNewName.GetValue()
        if len(id) == 0:
            self.success("编号不可为空")
            return
        if len(name) == 0:
            self.success("学院名不可为空")
            return
        # 连接数据库
        i = self.db.collegeInsert(id, name)
        self.db.commit()
        if i > 0:
            self.success("新增成功")
        else:
            self.success("新增失败，请检查")

    def OnDelete(self, event):
        if self.gridSelectId is not None:
            i = self.db.collegeDelete(self.gridSelectId)
            self.db.commit()
            if i > 0:
                self.success("删除成功")

    def OnFlash(self, event):
        self.success("当前未选择")
        self.textReName.SetLabel("")

    def success(self, value, flag=False):
        self.staticText1.SetLabel(value)
        self.textReName.SetEditable(flag)
        self.data = self.db.collegeSelectAll()
        self.grid.updateData(self.data)
        print("%s %s %s" % (self.gridSelectId, self.textReName.GetValue(), value))
