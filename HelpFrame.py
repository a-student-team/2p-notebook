import wx
import wx.html2
from get_file import get_file
class HelpFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="帮助", size=(600, 400))
        html = wx.html2.WebView.New(self)
        html.LoadURL(get_file("\\html\\help.html"))
        html.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.OnLoaded)
        # 将html控件添加到布局管理器中
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Show()
        icon = wx.Icon(get_file('\\images\\icon.ico'), wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
    def OnLoaded(self, event):
        pass
