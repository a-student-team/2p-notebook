import wx
from wx import html2
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
        self.browser = html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Centre(wx.BOTH)



class EditFrame(EditFrame1):
    # ui edit note
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, size=wx.DefaultSize, pos=wx.DefaultPosition, paper_title="title"):
        EditFrame1.__init__(self, parent, id, title, size, pos)
        self.paper_title = paper_title
        self.Bind(html2.EVT_WEBVIEW_LOADED, self.OnPageLoaded,
                  self.browser)

    def OnPageLoaded(self, event):
        event.Skip()