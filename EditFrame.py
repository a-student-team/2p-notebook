from tkinter.ttk import Style
import wx
from wx import html2
from get_file import get_file


class EditPanel(wx.Panel):

    def __init__(self,
                 parent,
                 size=(700, 700),
                 paper_title="title",
                 ):
        super().__init__(parent, wx.ID_ANY, wx.DefaultPosition, size,
                         wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = html2.WebView.New(self, style=wx.BORDER_NONE)
         
        sizer.Add(self.browser, 1, wx.EXPAND|wx.ALL, 0)
        self.SetSizer(sizer)
        self.Centre(wx.BOTH)

        self.paper_title = paper_title
        self.Bind(html2.EVT_WEBVIEW_LOADED, self.OnPageLoaded, self.browser)
        
        

    def OnPageLoaded(self, event):
        event.Skip()


class EditFrame1(wx.Frame):
    # edit note frame
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        title=wx.EmptyString,
        size=wx.DefaultSize,
        pos=wx.DefaultPosition,
    ):
        # import ./hmtl/edit.html and show
        # use html2

        wx.Frame.__init__(self,
                          parent,
                          id=id,
                          title=title,
                          size=size,
                          pos=pos,
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        #on main window
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = html2.WebView.New(self, style=wx.BORDER_NONE)
        #取消边框

        sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Centre(wx.BOTH)


class EditFrame(EditFrame1):
    # ui edit note
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 size=wx.DefaultSize,
                 pos=wx.DefaultPosition,
                 paper_title="title"):
        EditFrame1.__init__(self, parent, id, title, size, pos)
        self.paper_title = paper_title
        self.Bind(html2.EVT_WEBVIEW_LOADED, self.OnPageLoaded, self.browser)
        icon = wx.Icon(get_file('\\images\\icon.ico'), wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

    def OnPageLoaded(self, event):
        event.Skip()


#test EditPanel
if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None)
    panel = EditPanel(frame)
    frame.Show()
    app.MainLoop()