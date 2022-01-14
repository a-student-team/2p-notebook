import wx
class EncryptDialog(wx.Dialog):
    '''
    让用户输入密码
    '''
    def __init__(self, parent, value=""):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(200, 200), style=wx.DEFAULT_DIALOG_STYLE)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"请输入密码:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, str(value), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl1, 0, wx.ALL, 5)
        #确定按钮
        self.m_button5 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        self.SetSizer(bSizer5)
        self.Layout()
        self.Centre(wx.BOTH)
        self.m_button5.Bind(wx.EVT_BUTTON, self.close)
    
    def close(self, event):
        
        self.Destroy()