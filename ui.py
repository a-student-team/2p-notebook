# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!(no)
###########################################################################

import wx
from wx.core import BLACK
import wx.xrc
from wx import html2

import os


def get_file(file_name):
    '''
    :param file_name: relative file path, like '\\data\\test.txt'
    :return: file path
    '''
    return os.path.dirname(os.path.abspath(__file__)) + file_name


###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1(wx.Frame):
    ID_THEME = wx.NewId()
    ID_SETTING = wx.NewId()
    ID_THEME_DEFAULT = wx.NewId()
    ID_THEME_DARK = wx.NewId()
    ID_THEME_LIGHT = wx.NewId()
    ID_THEME_OTHER = wx.NewId()

    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=u"NoteBook",
                          pos=wx.DefaultPosition,
                          size=wx.Size(1000, 700),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.theme = {
            "kind": 1,
            "default_font": {
                "size": 18,
                "family": "wx.FONTFAMILY_DEFAULT",
                "style": "wx.FONTSTYLE_NORMAL",
                "weight": "wx.FONTWEIGHT_NORMAL",
                "underline": "false",
                "face_name": "Microsoft YaHei UI",
                "colour": "(247, 247, 247)"
            },
            "notebook_left": {
                "colour":
                "wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME)"
            },
            "notebook_right": {
                "colour": "(247, 247, 247)"
            },
            "morning_night_topic": {
                "colour": "(0, 0, 0)",
                "size": 75
            },
            "time_text": {
                "colour": "(0, 0, 0)",
                "size": 15
            }
        }  # theme dict
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                    "Microsoft YaHei UI"))
        self.SetMinSize(wx.Size(600, 400))

        menubar = wx.MenuBar(0)
        toolMenu = wx.Menu()
        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        newMenu = wx.Menu()
        self.nearlyfileMenu = wx.Menu()
        newMenu.Append(wx.ID_NEW, u"新建笔记", wx.EmptyString, wx.ITEM_NORMAL)
        newMenu.Append(wx.ID_FILE, u"新建笔记本", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(wx.ID_ANY, u"新建", newMenu)
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_OPEN, u"打开", wx.EmptyString, wx.ITEM_NORMAL)
        #tool menu
        thememenu = wx.Menu()
        thememenu.Append(self.ID_THEME_DEFAULT, u"默认主题", wx.EmptyString,
                         wx.ITEM_RADIO)
        thememenu.Append(self.ID_THEME_DARK, u"深色主题", wx.EmptyString,
                         wx.ITEM_RADIO)
        thememenu.Append(self.ID_THEME_LIGHT, u"浅色主题", wx.EmptyString,
                         wx.ITEM_RADIO)
        thememenu.Append(self.ID_THEME_OTHER, u"其他主题...", wx.EmptyString,
                         wx.ITEM_NORMAL)
        toolMenu.Append(self.ID_THEME, u"更换主题", thememenu)
        toolMenu.Append(self.ID_SETTING, u"设置", wx.EmptyString, wx.ITEM_NORMAL)
        #help menu
        helpMenu.Append(wx.ID_ABOUT, u"关于", wx.EmptyString, wx.ITEM_NORMAL)

        #nearly open

        self.file1 = wx.MenuItem(self.nearlyfileMenu, wx.ID_FILE1, u" ",
                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.file2 = wx.MenuItem(self.nearlyfileMenu, wx.ID_FILE2, u" ",
                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.file3 = wx.MenuItem(self.nearlyfileMenu, wx.ID_FILE3, u" ",
                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.file4 = wx.MenuItem(self.nearlyfileMenu, wx.ID_FILE4, u" ",
                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.file5 = wx.MenuItem(self.nearlyfileMenu, wx.ID_FILE5, u" ",
                                 wx.EmptyString, wx.ITEM_NORMAL)
        self.nearlyfileMenu.Append(self.file1)
        self.nearlyfileMenu.Append(self.file2)
        self.nearlyfileMenu.Append(self.file3)
        self.nearlyfileMenu.Append(self.file4)
        self.nearlyfileMenu.Append(self.file5)

        fileMenu.Append(wx.ID_ANY, u"最近打开", self.nearlyfileMenu)

        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_SAVE, u"保存", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(wx.ID_SAVEAS, u"另存为", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_EXIT, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        menubar.Append(fileMenu, u"文件")
        menubar.Append(toolMenu, u"工具")
        menubar.Append(helpMenu, u"关于")

        self.SetMenuBar(menubar)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel10 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                  wx.Size(150, 700), wx.TAB_TRAVERSAL)
        self.m_panel10.SetBackgroundColour(
            (wx.Colour(eval(self.theme["notebook_left"]["colour"]))))

        self.m_panel10.SetMinSize(wx.Size(200, 500))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer5.SetMinSize(wx.Size(200, 500))
        self.m_staticText9 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"我的笔记",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(
            wx.Font(
                24, eval(self.theme["default_font"]["family"]),
                eval(self.theme["default_font"]["style"]),
                eval(self.theme["default_font"]["weight"]), False if
                self.theme["default_font"]["underline"] == "false" else True,
                self.theme["default_font"]["face_name"]))
        self.m_staticText9.SetForegroundColour(
            wx.Colour(eval(self.theme["default_font"]["colour"])))

        bSizer5.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
                    5)

        self.note_list = NewNoteList(self.m_panel10)
        self.note_list.SetForegroundColour(
            wx.Colour(eval(self.theme["default_font"]["colour"])))
        self.note_list.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_left"]["colour"])))
        self.note_list.SetFont(
            wx.Font(
                13, eval(self.theme["default_font"]["family"]),
                eval(self.theme["default_font"]["style"]),
                eval(self.theme["default_font"]["weight"]), False if
                self.theme["default_font"]["underline"] == "false" else True,
                self.theme["default_font"]["face_name"]))

        bSizer5.Add(self.note_list, 0, wx.ALL, 5)

        self.m_panel10.SetSizer(bSizer5)
        self.m_panel10.Layout()
        gbSizer1.Add(self.m_panel10, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.ALL, 0)

        self.m_panel26 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                  wx.Size(700, 700), wx.TAB_TRAVERSAL)
        self.m_panel26.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.morning_night = wx.StaticText(self.m_panel26, wx.ID_ANY, u"早上好",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.morning_night.Wrap(-1)

        self.morning_night.SetFont(
            wx.Font(
                self.theme["morning_night_topic"]["size"],
                eval(self.theme["default_font"]["family"]),
                eval(self.theme["default_font"]["style"]),
                eval(self.theme["default_font"]["weight"]), False if
                self.theme["default_font"]["underline"] == "false" else True,
                self.theme["default_font"]["face_name"]))
        self.morning_night.SetForegroundColour(
            wx.Colour(eval(self.theme["morning_night_topic"]["colour"])))

        gbSizer2.Add(self.morning_night, wx.GBPosition(0, 0), wx.GBSpan(1, 2),
                     wx.ALL, 10)

        self.time_text = wx.StaticText(self.m_panel26, wx.ID_ANY, u"time",
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.time_text.Wrap(-1)

        self.time_text.SetFont(
            wx.Font(
                self.theme["time_text"]["size"],
                eval(self.theme["default_font"]["family"]),
                eval(self.theme["default_font"]["style"]),
                eval(self.theme["default_font"]["weight"]), False if
                self.theme["default_font"]["underline"] == "false" else True,
                self.theme["default_font"]["face_name"]))
        self.time_text.SetForegroundColour(
            wx.Colour(eval(self.theme["time_text"]["colour"])))

        gbSizer2.Add(self.time_text, wx.GBPosition(0, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button1 = wx.Button(
            self.m_panel26, wx.ID_ANY, u"添加新的笔记", wx.DefaultPosition,
            wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)

        self.m_button1.SetBitmapFocus(wx.NullBitmap)
        self.m_button1.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button1, wx.GBPosition(1, 0), wx.GBSpan(1, 1),
                     wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button11 = wx.Button(
            self.m_panel26, wx.ID_ANY, u"添加新的笔记本", wx.DefaultPosition,
            wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)
        self.m_button11.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button11, wx.GBPosition(2, 0), wx.GBSpan(1, 1),
                     wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button111 = wx.Button(
            self.m_panel26, wx.ID_ANY, u"添加新的便签", wx.DefaultPosition,
            wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)
        self.m_button111.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button111, wx.GBPosition(3, 0), wx.GBSpan(1, 1),
                     wx.ALL, 15)

        self.m_panel26.SetSizer(gbSizer2)

        self.m_panel26.Layout()
        gbSizer1.Add(self.m_panel26, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.ALL, 0)

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        gbSizer1.AddGrowableRow(0)
        gbSizer1.AddGrowableCol(1)

        gbSizer2.AddGrowableRow(3)
        gbSizer2.AddGrowableCol(2)

        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.change_time, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔为1秒

        # Connect Events

        self.m_button1.Bind(wx.EVT_BUTTON, self.new_paper)
        self.m_button11.Bind(wx.EVT_BUTTON, self.new_book)
        self.m_button111.Bind(wx.EVT_BUTTON, self.new_note)
        self.note_list.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.edit_note)
        self.note_list.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.edit_note_end)
        self.m_panel10.Bind(wx.EVT_RIGHT_DOWN, self.show_menu)
        self.note_list.Bind(wx.EVT_RIGHT_DOWN, self.show_menu)
        self.Bind(wx.EVT_MENU, self.menuHandler)
        self.note_list.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.open_note)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.note_list.Bind(wx.EVT_TREE_SEL_CHANGED, self.note_list_is_changed)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def note_list_is_changed(self, event):
        event.Skip()

    def on_close(self, event):
        event.Skip()

    def open_note(self, event):
        event.Skip()

    def change_time(self, event):
        event.Skip()

    def show_menu(self, event):
        event.Skip()

    def menuHandler(self, event):
        event.Skip()

    def edit_note(self, event):
        event.Veto()

    def edit_note_end(self, event):
        event.Veto()

    def new_paper(self, event):
        event.Skip()

    def new_book(self, event):
        event.Skip()

    def new_note(self, event):
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
        self.browser = html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        self.Centre(wx.BOTH)


class NoBorderFrame(wx.Frame):
    # a frame that has a sizer without borders
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.NO_BORDER,
                 name=wx.FrameNameStr):
        wx.Frame.__init__(self,
                          parent,
                          id=id,
                          title=title,
                          size=size,
                          pos=pos,
                          style=style,
                          name=name)

        self.Center()
        self.Show(True)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        # a sizer like windows title bar
        self.sizer = wx.GridSizer(0, 0, 0, 0)

        # close button
        self.close_bitmap = wx.Bitmap(get_file('\\images\\close.png'),
                                      wx.BITMAP_TYPE_PNG)

        self.close_button = wx.BitmapButton(
            self,
            wx.ID_ANY,
            self.close_bitmap,
            style=wx.BU_AUTODRAW | wx.BORDER_NONE | wx.BU_RIGHT,
            size=(self.close_bitmap.GetWidth() + 5,
                  self.close_bitmap.GetHeight() + 5))
        # set background color like frame
        self.close_button.SetBackgroundColour(self.GetBackgroundColour())
        self.close_button.SetBitmapFocus(
            wx.Bitmap(get_file('\\images\\close_focus.png'),
                      wx.BITMAP_TYPE_PNG))

        self.sizer.Add(self.close_button, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.Layout()
        self.main_sizer.Add(self.sizer, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.print_screen()
        self.SetSizer(self.main_sizer)

        self.Layout()

        # bind events
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

    def print_screen(self):
        pass

    def OnClose(self, event):
        self.Destroy()

    def OnMouse(self, event):
        # move like windows title bar
        if event.LeftDown():
            self.CaptureMouse()
            self.pos = event.GetPosition()

        elif event.LeftUp():
            self.ReleaseMouse()
        #move like windows title bar
        elif event.Dragging():
            if self.HasCapture():
                pos = event.GetPosition()

                self.Move(self.GetPosition() + event.GetPosition())
                self.pos = pos
        '''if event.LeftDown():
            self.CaptureMouse()
            self.pos = event.GetPosition()
        elif event.LeftUp():
            self.ReleaseMouse()
        elif event.Dragging():
            if self.HasCapture():
                self.Move(self.GetPosition() + event.GetPosition())
                self.pos = event.GetPosition()
        event.Skip()'''


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


class SettingFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self,
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
        text = wx.StaticText(self.theme, wx.ID_ANY, u"外观设置不知道写啥的屑",
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


class NewNoteList(wx.TreeCtrl):
    '''
    重写树, 使其变得更加美观
    '''

    def __init__(self, parent):
        super().__init__(
            parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 700),
            wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT
            | wx.TR_NO_LINES | wx.BORDER_NONE | wx.WANTS_CHARS | wx.TR_SINGLE
            | wx.EXPAND | wx.HSCROLL)
        self.SetFont(
            wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        #Each second level item item has a box with all its children
        pass


class MyApp(wx.App):

    def OnInit(self):
        MyFrame1(None).Show()

        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
