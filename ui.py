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
import wx.lib.agw.customtreectrl as treectrl
from EditFrame import EditFrame as EditFrame1

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

        helpMenu.Append(wx.ID_HELP, u"帮助", wx.EmptyString, wx.ITEM_NORMAL)
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

        bSizer5.Add(self.note_list, 0, wx.ALL, 0)

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









class NewNoteList(treectrl.CustomTreeCtrl):
    '''
    一个树罢了
    '''

    def __init__(self, parent):
        super().__init__(
            parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 700), agwStyle=treectrl.TR_HAS_BUTTONS|treectrl.TR_FULL_ROW_HIGHLIGHT|treectrl.TR_ELLIPSIZE_LONG_ITEMS|treectrl.TR_TOOLTIP_ON_LONG_ITEMS
            |treectrl.TR_HAS_VARIABLE_ROW_HEIGHT)
        panel_font = self.GetFont()
        panel_font.SetPointSize(panel_font.GetPointSize() + 1)
        self.SetFont(panel_font)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.EnableSelectionGradient(False)
        self.SetSpacing(20)
        self.SetIndent(10)
        self.SetImageList(wx.ImageList(16, 16))

        
        


        


class MyApp(wx.App):

    def OnInit(self):
        MyFrame1(None).Show()

        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
