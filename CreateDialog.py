import wx
class CreateDialog (wx.Dialog):  # 名字输入框

    def __init__(self, parent, value="", encrypt=False):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(171, 170), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(100, 250), wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"请输入名字:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, str(value), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #让用户选择是否加密
        self.m_checkBox1 = wx.CheckBox(
            self, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox1.SetValue(True)
        if encrypt == True:
            
            bSizer5.Add(self.m_checkBox1, 0, wx.ALL, 5)
        else:
            self.m_checkBox1.Hide()
        #确定按钮
        self.m_button5 = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        


        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button5.Bind(wx.EVT_BUTTON, self.note_name)
        self.Bind(wx.EVT_CLOSE, self.close)

        self.ShowModal()

    def note_name(self, event):
        self.Destroy()

    def __del__(self):
        pass

    def close(self, event):
        
        self.Destroy()