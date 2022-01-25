import wx
from wx import html2
from get_file import get_file
from wx.richtext import RichTextCtrl


class EditPanel(wx.Panel):

    def __init__(self,
                 parent,
                 size=(700, 700),
                 paper_title="title",
                 ):
        super().__init__(parent, wx.ID_ANY, wx.DefaultPosition, size,
                         wx.TAB_TRAVERSAL)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = html2.WebView.New(self, style=wx.BORDER_NONE)
        self.browser.LoadURL(get_file("\\html\\edit.html"))
        self.sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(self.sizer)

        self.paper_title = paper_title
        #self._init_ui()

        self.bold = False
'''        
        

    def _init_ui(self):
        #实现wxpyhton与html2的交互
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.bold = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\bold.png"), wx.BITMAP_TYPE_PNG))
        self.italic = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\italic.png"), wx.BITMAP_TYPE_PNG))
        self.underline = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\underline.png"), wx.BITMAP_TYPE_PNG))
        self.font_size = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\font size.png"), wx.BITMAP_TYPE_PNG))
        self.font_color = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\font color.png"), wx.BITMAP_TYPE_PNG))
        self.align_left = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\align left.png"), wx.BITMAP_TYPE_PNG))
        self.align_center = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\align center.png"), wx.BITMAP_TYPE_PNG))
        self.align_right = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\align right.png"), wx.BITMAP_TYPE_PNG))
        self.align_both = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\align both.png"), wx.BITMAP_TYPE_PNG))
        self.indent = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\indent.png"), wx.BITMAP_TYPE_PNG))
        self.outdent = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\outdent.png"), wx.BITMAP_TYPE_PNG))
        self.text_book = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\text.png"), wx.BITMAP_TYPE_PNG))
        self.code = wx.BitmapButton(self, -1, wx.Bitmap(get_file("\\images\\code.png"), wx.BITMAP_TYPE_PNG))
        self.button_sizer.Add(self.bold, 0, wx.ALL, 5)
        self.button_sizer.Add(self.italic, 0, wx.ALL, 5)
        self.button_sizer.Add(self.underline, 0, wx.ALL, 5)
        self.button_sizer.Add(self.font_size, 0, wx.ALL, 5)
        self.button_sizer.Add(self.font_color, 0, wx.ALL, 5)
        self.button_sizer.Add(self.align_left, 0, wx.ALL, 5)
        self.button_sizer.Add(self.align_center, 0, wx.ALL, 5)
        self.button_sizer.Add(self.align_right, 0, wx.ALL, 5)
        self.button_sizer.Add(self.align_both, 0, wx.ALL, 5)
        self.button_sizer.Add(self.indent, 0, wx.ALL, 5)
        self.button_sizer.Add(self.outdent, 0, wx.ALL, 5)
        self.button_sizer.Add(self.text_book, 0, wx.ALL, 5)
        self.button_sizer.Add(self.code, 0, wx.ALL, 5)
        self.sizer.Add(self.button_sizer, 0, wx.ALL, 5)
        self.rich_textctrl = RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                        wx.TE_MULTILINE | wx.TE_RICH2| wx.BORDER_NONE)
        self.sizer.Add(self.rich_textctrl, 1, wx.EXPAND, 0)
        self.Layout()
        #Bind
        self.Bind(wx.EVT_BUTTON, self.OnBold, self.bold)
    

        self.Bind(wx.EVT_BUTTON, self.OnItalic, self.italic)
        self.Bind(wx.EVT_BUTTON, self.OnUnderline, self.underline)
        self.Bind(wx.EVT_BUTTON, self.OnFontSize, self.font_size)
        self.Bind(wx.EVT_BUTTON, self.OnFontColor, self.font_color)
        self.Bind(wx.EVT_BUTTON, self.OnAlignLeft, self.align_left)
        self.Bind(wx.EVT_BUTTON, self.OnAlignCenter, self.align_center)
        self.Bind(wx.EVT_BUTTON, self.OnAlignRight, self.align_right)
        self.Bind(wx.EVT_BUTTON, self.OnAlignBoth, self.align_both)
        self.Bind(wx.EVT_BUTTON, self.OnIndent, self.indent)
        self.Bind(wx.EVT_BUTTON, self.OnOutdent, self.outdent)
        self.Bind(wx.EVT_BUTTON, self.OnTextBook, self.text_book)
        self.Bind(wx.EVT_BUTTON, self.OnCode, self.code)
    def OnBold(self, event):
        if self.bold == True:
            self.bold = False
            self.rich_textctrl.EndBold()
            return None
        selection = self.rich_textctrl.GetSelectionRange()
        
        if selection == (-2, -2):
            self.rich_textctrl.BeginBold()
            self.bold = True
        else:
            #bold the selection text
            self.rich_textctrl.BeginBold()
            self.rich_textctrl.EndBold()'''

            
'''
    def OnPageLoaded(self, event):
        event.Skip()'''


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
        self.browser.LoadURL(get_file("\\html\\edit.html"))
        #取消边框

        sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        


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
        self.Centre(wx.BOTH)
        

    def OnPageLoaded(self, event):
        event.Skip()

#test EditPanel
if __name__ == '__main__':
    app = wx.App()
    frame = EditFrame(None)
    frame.Show()
    sizer = wx.BoxSizer()
    panel = wx.Panel(frame)
    panel_sizer = wx.BoxSizer(wx.VERTICAL)
    browser = html2.WebView.New(panel, style=wx.BORDER_NONE)
    browser.LoadURL(get_file('\\html\\edit.html'))
    panel_sizer.Add(browser, 1, wx.EXPAND, 0)
    panel.SetSizer(panel_sizer)
    sizer.Add(panel, 1, wx.EXPAND, 0)
    
    app.MainLoop()