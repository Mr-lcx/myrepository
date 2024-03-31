

import wx
from Frm_login.frm_login import LoginFrame


class App(wx.App):
    def OnInit(self):
        frame = LoginFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
