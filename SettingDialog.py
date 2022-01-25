import wx
class SettingDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=wx.EmptyString,
                          pos=wx.DefaultPosition,
                          size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.basic = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition,
                              wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.basic, u"基础", False)
        self.theme = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition,
                              wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.theme, u"外观", False)
        self.file = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition,
                             wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.file, u"存储", False)
        self.more = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition,
                             wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.more, u"更多", False)

        bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self._init_basic_page()
        self._init_theme_page()
        self._init_file_page()
        self._init_more_page()

    def _init_basic_page(self):
        # basic page
        self.basic_sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self.basic, wx.ID_ANY, u"基础设置不知道写啥的屑",
                             wx.DefaultPosition, wx.DefaultSize, 0)
        text.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.basic_sizer.Add(text, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.basic.SetSizer(self.basic_sizer)
        self.basic.Layout()

    def _init_theme_page(self):
        # theme page
        self.theme_sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self.theme, wx.ID_ANY, u"主题设置不知道写啥的屑",
                             wx.DefaultPosition, wx.DefaultSize, 0)
        text.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.theme_sizer.Add(text, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        
        self.theme.SetSizer(self.theme_sizer)
        self.theme.Layout()

    def _init_file_page(self):
        # file page
        self.file_sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self.file, wx.ID_ANY, u"存储设置不知道写啥的屑",
                             wx.DefaultPosition, wx.DefaultSize, 0)
        text.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.file_sizer.Add(text, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.file.SetSizer(self.file_sizer)
        self.file.Layout()

    def _init_more_page(self):
        # more page
        self.more_sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self.more, wx.ID_ANY, u"没有更多", wx.DefaultPosition,
                             wx.DefaultSize, 0)
        text.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.more_sizer.Add(text, 0, wx.ALL | wx.ALIGN_CENTER, 5)
        self.more.SetSizer(self.more_sizer)
        self.more.Layout()

    def open(self, page):
        #open a page in notebook
        self.m_notebook1.SetSelection(page)
