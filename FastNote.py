import wx
from NoBorderFrame import NoBorderFrame
class FastNote(NoBorderFrame):  # 便签

    def __init__(self, parent):
        
        NoBorderFrame.__init__(self,
                               parent,
                               id=wx.ID_ANY,
                               pos=wx.DefaultPosition,
                               size=wx.Size(200, 200))
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.Centre(wx.BOTH)

    def print_title_sizer(self):
        self.font_size_btn = wx.Button(self,
                                        wx.ID_ANY,
                                        'A',
                                        size=(30, 30),
                                        style=wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.font_size_btn.SetBackgroundColour(self.GetBackgroundColour())
        self.font_size_btn.Bind(wx.EVT_ENTER_WINDOW, self.enter_window)
        self.font_size_btn.Bind(wx.EVT_LEAVE_WINDOW, self.leave_window)
        self.sizer.Add(self.font_size_btn, 0, wx.ALL | wx.ALIGN_LEFT, 0)
        self.font_size_btn.Bind(wx.EVT_BUTTON, self.OnFontSize)
    def leave_window(self, event):
        self.font_size_btn.SetBackgroundColour(self.GetBackgroundColour())
        self.font_size_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.font_size_btn.Refresh()
        event.Skip()
    def enter_window(self, event):
        self.font_size_btn.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.font_size_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.font_size_btn.Refresh()
        event.Skip()
    def OnFontSize(self, event):
        #修改字体大小
        
        font_size = wx.GetNumberFromUser('输入字体大小', '字体大小', '字体大小',
                                            self.m_textCtrl2.GetFont().GetPointSize(),
                                            1,
                                            100)
        if font_size > 0:
            self.m_textCtrl2.SetFont(wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                                wx.FONTSTYLE_NORMAL,
                                                wx.FONTWEIGHT_NORMAL, False,
                                                "Microsoft YaHei UI"))
            self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))
            self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
            self.m_textCtrl2.SetValue(self.m_textCtrl2.GetValue())
            self.m_textCtrl2.Refresh()
            self.Layout()

        

    def print_screen(self):

        self.m_textCtrl2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       wx.EmptyString,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       style=wx.NO_BORDER|wx.TE_MULTILINE)
        
        self.m_textCtrl2.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        
        self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
        self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))

        self.main_sizer.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(self.main_sizer)

        self.Layout()

    def __del__(self):
        pass

#test
if __name__ == '__main__':
    app = wx.App()
    frame = FastNote(None)
    frame.Show()
    app.MainLoop()

