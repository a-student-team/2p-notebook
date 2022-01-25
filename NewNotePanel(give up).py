import wx
from EditFrame import EditFrame
from wx import html2
from get_file import get_file
from NewNoteList import NewNoteList
from CreateDialog import CreateDialog


class NoteListPanel(wx.Panel):
    '''
    通过note_list映射出frame显示到屏幕上
    '''
    
    def __init__(self, parent, note_list, note_data):
        super().__init__(parent)
        self.note_list = note_list
        self.note_list_sizer = wx.BoxSizer(wx.VERTICAL)
        self.note_data = note_data #eg:{"topic1":{topic2:content}}

        self.focused = None #当前选中的note
        self.count = 0 #note的数量


        self.SetSizer(self.note_list_sizer)
        self.note_list_ui = {}
        self.SetSize(wx.Size(250, 700))
        self._init_ui()
        
        self.SetSizer(self.note_list_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        
    def sort_list(self):
        self.note_list.SortChildren(self.note_list.GetRootItem())
        self.Refresh()

    def Refresh(
        self,
        eraseBackground=True,
        rect=None,
        colour={
            "font": "(0, 0, 0)",
            "background":
            "wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME)"
        }):

        #refresh the ui and init the ui
        self.note_list_sizer.Destroy()
        self.note_list_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.note_list_sizer)
        self.count = 0
        self.note_list_ui = {}
        self._init_ui()
        for i in self.note_list_ui.values():
            if type(i) == wx.WrapSizer:
                continue
            print(i)
            i.SetForegroundColour(wx.Colour(eval(colour["font"])))

        for i in self.note_list_ui.values():
            if type(i) == wx.WrapSizer:
                continue
            i.SetBackgroundColour(wx.Colour(eval(
                colour["background"])))  #设置成跟背景一样的颜色
        self.Layout()

        

    def SetForegroundColour(self, colour):
        super().SetForegroundColour(colour)
        for i in self.note_list_ui.values():
            print(i)
            try:
                i.SetForegroundColour(colour)
            except:
                continue
        return True

    def SetBackgroundColour(self, colour):
        super().SetBackgroundColour(colour)
        for i in self.note_list_ui.values():
            try:
                i.SetBackgroundColour(colour)
            except:
                continue
        return True

    def _init_ui(self):
        
        #use note_list to print ui
        try:
            for i in self.note_list.ergodic():
                print(i)
                if i[2] == 1:
                    continue
                get = self.SecondLevelItemUI(self, i[1])
                self.note_list_ui[i[1]] = get
                self.note_list_sizer.Add(get, 0, wx.ALIGN_LEFT, 0)
                self.count += 1
                for j in self.note_list.ergodic_item(i[0]):
                    print(j)
                    get = self.NormaleItemUI(self, j[1], j[0],self.note_data[i[1]][j[1]], self.note_list)
                    self.note_list_ui[j[1]] = get
                    self.note_list_sizer.Add(get, 0, wx.LEFT | wx.ALIGN_LEFT,
                                                25)
                    self.count += 1
            self.Layout()
        except:
            return False
        
        #设置foucsed机制
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        

    def OnLeftDown(self, event):
        #设置focus
        item, flags = self.note_list.HitTest(event.GetPosition())
        if item:
            self.note_list.SelectItem(item)
            self.focused = item
            self.Refresh()
        print(self.focused)
        event.Skip()

        
    def new_paper(self, panel):
         # get selected item and append new item in it
        root = panel
        

        try:
            # if root is paper, root = root.parent
            if self.note_list.GetItemParent(root) != self.note_list.GetRootItem():
                root = self.note_list.GetItemParent(root)
            
            self.note_list.Expand(root)
            self.note_list.ExpandAll()
        except:
            dialog = wx.MessageDialog(
                self, '请选择笔记本', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None

        name = CreateDialog(self, "新笔记").m_textCtrl1.GetValue()

        if name == '':
            return None

        if self._note_in_note_data(name, self.note_list.GetItemText(root)):
            dialog = wx.MessageDialog(
                self, '名字重复啦, 笔记已存在', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None
        #print(self.note_data[self.note_list.GetItemText(root)])

        self.note_list.AppendItem(root, name)

        self.note_list.Expand(root)
        self.note_list.ExpandAll()

        self.note_data[self.note_list.GetItemText(root)][name] = '内容'

        self.sort_list()
        self.Update()
        self.Refresh()
       
        

    class NormaleItemUI(wx.Panel):
        def __init__(self, parent, item_name, note_list_item, item_content="content", note_list=None):
            super().__init__(parent)
            self.item_name = item_name
            self.note_list_item = note_list_item
            self.item_content = item_content
            self.note_list = note_list
            self._normal_item_ui(item_name, note_list_item, item_content)
            
        def _normal_item_ui(self, item_str, note_list_item=None, content="content"):
            self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                            wx.Size(150, 50), wx.TAB_TRAVERSAL)
            self.panel.SetBackgroundColour(wx.Colour(239, 239, 239))

            bSizer2 = wx.BoxSizer(wx.VERTICAL)

            self.topic_statictext = wx.StaticText(self.panel, wx.ID_ANY,
                                        u"{}".format(item_str),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
            self.topic_statictext.Wrap(-1)
            self.topic_statictext.SetFont(
                wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

            bSizer2.Add(self.topic_statictext, 0, wx.ALL, 0)

            self.content_statictext = wx.StaticText(self.panel, wx.ID_ANY, u"{}".format(content),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
            self.content_statictext.Wrap(-1)
            self.content_statictext.SetFont(
                wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
            self.content_statictext.SetForegroundColour(wx.Colour(50, 51, 52))

            bSizer2.Add(self.content_statictext, 0, wx.ALL, 0)

            self.panel.SetSizer(bSizer2)
            self.panel.Layout()
            
            

            self.panel.Bind(wx.EVT_ENTER_WINDOW, lambda event:self.on_enter(event, self.panel))
            
            self.panel.Bind(wx.EVT_LEFT_DOWN, lambda event:self.on_click(event, self.panel, note_list_item))

            self.panel.Bind(wx.EVT_LEAVE_WINDOW, lambda event:self.on_leave(event, self.panel))
            


            return self.panel
        def on_enter(self, event, panel):
            #set the focus and background color, set other panel's background color to common color
            panel.SetBackgroundColour(wx.Colour(255, 255, 255))
            
            panel.SetFocus()
            
            print("enter")
            panel.Refresh()
            
        def on_leave(self, event, panel):
            
            panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
            print("leave")
            panel.Refresh()



        def on_click(self, event, panel, note_list_item=None):
            root = note_list_item
            
            if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
                return None
            if root == self.note_list.GetRootItem():
                return None
            else:
                #全屏
                edit_browser = EditFrame(self, title="编辑笔记", size=wx.Size(wx.GetDisplaySize())
                , paper_title=self.note_list.GetItemText(root))
                
                
                edit_browser.browser.LoadURL(get_file('\\html\\edit.html?text={}'.format(self.item_content)))
                edit_browser.Show()
                edit_browser.Bind(wx.EVT_CLOSE, lambda event: self.edit_browser_close(event, root))
                # when it open, give a value to edit_browser.browser
                edit_browser.Bind(html2.EVT_WEBVIEW_LOADED, lambda event: self.edit_browser_open(event, root))
        def edit_browser_open(self, event, root):
            event.Skip()
            
        def edit_browser_close(self, event, root):
            # when it close, get the value from edit_browser.browser
            event.Skip()

    class SecondLevelItemUI(wx.Panel):
        def __init__(self, parent, topic):
            super().__init__(parent)
            self.topic = topic
            self._second_level_ui(topic)
            
            self.Layout()
        def _second_level_ui(self, topic):
            
            wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

            m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                wx.Size(150, 50), wx.TAB_TRAVERSAL)
            m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

            bSizer2 = wx.BoxSizer(wx.VERTICAL)

            m_staticText2 = wx.StaticText(m_panel1, wx.ID_ANY, u"{}".format(topic),
                                        wx.DefaultPosition, wx.DefaultSize, 0)
            m_staticText2.Wrap(-1)
            m_staticText2.SetFont(
                wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                        wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

            bSizer2.Add(m_staticText2, 0, wx.ALL, 3)

            m_panel1.SetSizer(bSizer2)
            m_panel1.Layout()
            wSizer1.Add(m_panel1, 1, wx.EXPAND | wx.BOTTOM, 5)
            m_panel1.Bind(wx.EVT_ENTER_WINDOW, lambda event:self.on_enter(event, m_panel1))
            m_panel1.Bind(wx.EVT_LEAVE_WINDOW, lambda event:self.on_leave(event, m_panel1))

            return m_panel1
        def on_enter(self, event, panel):
            #set the focus and background color, set other panel's background color to common color
            panel.SetBackgroundColour(wx.Colour(255, 255, 255))
            
            panel.SetFocus()
            self.focused = panel
            print("enter")
            panel.Refresh()
            
        def on_leave(self, event, panel):
            
            panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
            print("leave")
            panel.Refresh()



    def on_click(self, event, panel, note_list_item=None):
        root = note_list_item
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            return None
        if root == self.note_list.GetRootItem():
            return None
        else:
            #全屏
            edit_browser = EditFrame(self, title="编辑笔记", size=wx.Size(wx.GetDisplaySize())
            , paper_title=self.note_list.GetItemText(root))
            
            
            edit_browser.browser.LoadURL(get_file('\\html\\edit.html?text={}'.format("")))
            edit_browser.Show()
            edit_browser.Bind(wx.EVT_CLOSE, lambda event: self.edit_browser_close(event, root))
            # when it open, give a value to edit_browser.browser
            edit_browser.Bind(html2.EVT_WEBVIEW_LOADED, lambda event: self.edit_browser_open(event, root))

#test
if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'test', size=(800, 1000))
    list = NewNoteList(frame)
    list.Hide()
    list.AddRoot("root")
    a = list.AppendItem(list.GetRootItem(), 'test1')

    list.AppendItem(list.GetRootItem(), 'test2')
    list.AppendItem(list.GetRootItem(), 'test3')
    list.AppendItem(list.GetRootItem(), 'test4')
    
    list.AppendItem(a, 'test11')
    print(list)
    note_data = {"test1":{"test11": "test"}, "test2": "test"}
    panel = NoteListPanel(frame, list, note_data)
    
    panel.Show()
    
    frame.Show()
    app.MainLoop()