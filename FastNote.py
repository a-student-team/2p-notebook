import wx
from NoBorderFrame import NoBorderFrame
class FastNote(NoBorderFrame):  # 便签

    def __init__(self, parent):
        NoBorderFrame.__init__(self,
                               parent,
                               id=wx.ID_ANY,
                               pos=wx.DefaultPosition,
                               size=wx.Size(200, 200))
        self.Centre(wx.BOTH)

    def print_screen(self):

        self.m_textCtrl2 = wx.TextCtrl(self,
                                       wx.ID_ANY,
                                       wx.EmptyString,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       style=wx.TE_MULTILINE)
        self.m_textCtrl2.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
        self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))

        self.main_sizer.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(self.main_sizer)

        self.Layout()

    def __del__(self):
        pass

