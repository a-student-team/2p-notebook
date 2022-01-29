# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!(no)
###########################################################################

import wx
import wx.xrc
from NewNoteList import NewNoteList
from static.MButton import MButton

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
    

    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=u"NoteBook",
                          pos=wx.DefaultPosition,
                          size=wx.Size(1000, 700),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.ID_THEME = wx.NewId()
        self.ID_SETTING = wx.NewId()
        self.ID_THEME_DEFAULT = wx.NewId()
        self.ID_THEME_DARK = wx.NewId()
        self.ID_THEME_LIGHT = wx.NewId()
        self.ID_THEME_OTHER = wx.NewId()
        self.ID_SELECT_OPEN = wx.NewId()
        self.ID_SELECT_SAVE = wx.NewId()
        self.theme = {
            "kind": 1,
            "default_font": {
                "size": 13,
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
        self.SetMinSize(wx.Size(1000, 700))
        self.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                    "Microsoft YaHei UI"))
        self.SetMinSize(wx.Size(600, 400))
        #添加图标
        icon = wx.Icon(get_file('\\images\\icon.ico'), wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.image_list = wx.ImageList(16, 16)
        self.image_list.Add(wx.Bitmap(get_file('\\images\\encrypted.png')))

        menubar = wx.MenuBar(0)
        toolMenu = wx.Menu()
        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        newMenu = wx.Menu()
        self.nearlyfileMenu = wx.Menu()
        newMenu.Append(wx.ID_NEW, u"新建笔记(&B)", wx.EmptyString, wx.ITEM_NORMAL)
        newMenu.Append(wx.ID_FILE, u"新建笔记本(&N)", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(wx.ID_ANY, u"新建", newMenu)
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_OPEN, u"打开(&O)", wx.EmptyString, wx.ITEM_NORMAL)
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
        fileMenu.Append(wx.ID_SAVE, u"保存(&S)", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(wx.ID_SAVEAS, u"另存为", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.AppendSeparator()
        fileMenu.Append(self.ID_SELECT_OPEN, u"选择导入", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(self.ID_SELECT_SAVE, u"选择导出", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_EXIT, u"退出", wx.EmptyString, wx.ITEM_NORMAL)

        helpMenu.Append(wx.ID_HELP, u"帮助", wx.EmptyString, wx.ITEM_NORMAL)
        helpMenu.Append(wx.ID_HELP_COMMANDS, u"反馈", wx.EmptyString, wx.ITEM_NORMAL)
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
        self.m_panel10.SetMaxSize(wx.Size(200, -1))

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

        #搜索框
        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel10, wx.ID_ANY,
                                             wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        self.m_searchCtrl1.ShowSearchButton(True)

        bSizer5.Add(self.m_searchCtrl1, 0, wx.ALL | wx.EXPAND,
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
        #image_list 
        self.note_list.AssignImageList(self.image_list)

        bSizer5.Add(self.note_list, 0, wx.ALL, 0)

        self.m_panel10.SetSizer(bSizer5)
        self.m_panel10.Layout()
        gbSizer1.Add(self.m_panel10, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.ALL, 0)
        


        self.m_panel26 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                  wx.Size(800, 700), wx.TAB_TRAVERSAL)
        self.m_panel26.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        '''self.edit_panel = EditPanel(self.m_panel26, size=wx.Size(800, 700))
        self.edit_panel.SetBackgroundColour(
            wx.Colour(0, 0, 0))
        self.edit_panel.browser.LoadURL(get_file("\\html\\edit.html"))'''
        
        
        self.gbSizer2_panel = wx.Panel(self.m_panel26, wx.ID_ANY,
                                        wx.DefaultPosition, wx.Size(800, 700),
                                        wx.TAB_TRAVERSAL)
        self.gbSizer2_panel.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
        

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.morning_night = wx.StaticText(self.gbSizer2_panel, wx.ID_ANY, u"早上好",
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

        self.time_text = wx.StaticText(self.gbSizer2_panel, wx.ID_ANY, u"time",
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
        

        gbSizer2.Add(self.time_text, wx.GBPosition(0, 2), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.welcome = wx.StaticText(self.gbSizer2_panel, wx.ID_ANY, u"欢迎使用笔记本, 你可以....",
                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.welcome.Wrap(-1)

        self.welcome.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"])
        )
        welcome_font_colour = eval(self.theme["default_font"]["colour"])
        #颜色取反
        welcome_font_colour = (255 - welcome_font_colour[0], 255 - welcome_font_colour[1], 255 - welcome_font_colour[2])
        self.welcome.SetForegroundColour(
            wx.Colour(welcome_font_colour))
        gbSizer2.Add(self.welcome, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_button1 = MButton(self.gbSizer2_panel, u"添加新的笔记",)
        #添加图标
        self.m_button1.SetBitmap(
            wx.Bitmap(
                get_file("\\images\\new_paper.png"),
                wx.BITMAP_TYPE_ANY))
        self.m_button1.SetBitmapMargins(0, 0)
        self.m_button1.SetBitmapPosition(wx.LEFT)
        

        
        self.m_button1.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.m_button1.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        gbSizer2.Add(self.m_button1, wx.GBPosition(2, 0), wx.GBSpan(1, 1),
                     wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button11 = MButton(
            self.gbSizer2_panel, u"添加新的笔记本", wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)
        self.m_button11.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.m_button11.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
        #添加图标
        self.m_button11.SetBitmap(
            wx.Bitmap(
                get_file("\\images\\new_book.png"),
                wx.BITMAP_TYPE_ANY))
        self.m_button11.SetBitmapMargins(0, 0)
        self.m_button11.SetBitmapPosition(wx.LEFT)

        gbSizer2.Add(self.m_button11, wx.GBPosition(3, 0), wx.GBSpan(1, 1),
                     wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.calendar_button = MButton(
            self.gbSizer2_panel, u"查看日程表", wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)
        self.calendar_button.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.calendar_button.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
        #添加图标
        self.calendar_button.SetBitmap(
            wx.Bitmap(
                get_file("\\images\\new_calendar.png"),
                wx.BITMAP_TYPE_ANY))
        self.calendar_button.SetBitmapMargins(0, 0)
        self.calendar_button.SetBitmapPosition(wx.LEFT)

        gbSizer2.Add(self.calendar_button, wx.GBPosition(4, 0), wx.GBSpan(1, 1),
                        wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button111 = MButton(
            self.gbSizer2_panel, u"添加新的便签", wx.BORDER_NONE | wx.BORDER_SIMPLE
            | wx.BORDER_THEME)
            
        self.m_button111.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.m_button111.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
        

        gbSizer2.Add(self.m_button111, wx.GBPosition(5, 0), wx.GBSpan(1, 1),
                     wx.ALL, 15)
        
                        

        self.help_text = wx.StaticText(self.gbSizer2_panel, wx.ID_ANY, u"更多",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.help_text.Wrap(-1)

        self.help_text.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"])
        )
        help_text_colour = eval(self.theme["default_font"]["colour"])
        
        #颜色取反
        help_text_colour = (255 - help_text_colour[0], 255 - help_text_colour[1], 255 - help_text_colour[2])
        self.help_text.SetForegroundColour(
            wx.Colour(help_text_colour))
        gbSizer2.Add(self.help_text, wx.GBPosition(6, 0), wx.GBSpan(1, 1),
                        wx.ALL, 5)
        self.help_button = MButton(self.gbSizer2_panel, u"帮助", wx.BORDER_NONE | wx.BORDER_SIMPLE
                                | wx.BORDER_THEME)
        self.help_button.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.help_button.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
        self.help_button.SetBitmap(
            wx.Bitmap(
                get_file("\\images\\help.png"),
                wx.BITMAP_TYPE_ANY))
        self.help_button.SetBitmapMargins(0, 0)
        self.help_button.SetBitmapPosition(wx.LEFT)

        self.nearly_open_text = wx.StaticText(self.gbSizer2_panel, wx.ID_ANY, u"你最近打开了...",
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.nearly_open_text.Wrap(-1)
        self.nearly_open_text.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"])
        )
        
        gbSizer2.Add(self.nearly_open_text, wx.GBPosition(1, 2), wx.GBSpan(1, 1),
                        wx.ALL, 5)
        
        self.nearly_open_button_more = MButton(self.gbSizer2_panel, u"查看更多", wx.BORDER_NONE)
        self.nearly_open_button_more.SetFont(
            wx.Font(self.theme["default_font"]["size"]-3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.nearly_open_button_more.default_fore = (98, 148, 193)
        self.nearly_open_button_more.default_back = eval(self.theme["notebook_right"]["colour"])
        self.nearly_open_button_more.enter_back = eval(self.theme["notebook_right"]["colour"])
        self.nearly_open_button_more.enter_fore = (46, 177, 240)
        self.nearly_open_button_more.refresh()

        
        

        self.nearly_open_button = MButton(self.gbSizer2_panel, u"", wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.nearly_open_button.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.nearly_open_button.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        self.nearly_open_button2 = MButton(self.gbSizer2_panel, u"", wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.nearly_open_button2.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.nearly_open_button2.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        self.nearly_open_button3 = MButton(self.gbSizer2_panel,  u"", wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.nearly_open_button3.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.nearly_open_button3.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        self.nearly_open_button4 = MButton(self.gbSizer2_panel, u"", wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.nearly_open_button4.SetFont(
            wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
        self.nearly_open_button4.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))

        self.nearly_open_button.file_path = ""
        self.nearly_open_button2.file_path = ""
        self.nearly_open_button3.file_path = ""
        self.nearly_open_button4.file_path = ""

        

        gbSizer2.Add(self.nearly_open_button_more, wx.GBPosition(1, 3), wx.GBSpan(1, 1),
                        wx.ALL|wx.ALIGN_BOTTOM, 1)
        gbSizer2.Add(self.nearly_open_button, wx.GBPosition(2, 2), wx.GBSpan(1, 2),
                        wx.ALL, 5)
        gbSizer2.Add(self.nearly_open_button2, wx.GBPosition(3, 2), wx.GBSpan(1, 2),
                        wx.ALL, 5)
        gbSizer2.Add(self.nearly_open_button3, wx.GBPosition(4, 2), wx.GBSpan(1, 2),    
                        wx.ALL, 5)
        gbSizer2.Add(self.nearly_open_button4, wx.GBPosition(5, 2), wx.GBSpan(1, 2),
                        wx.ALL, 5)
        
        

        


        
        
        gbSizer2.Add(self.help_button, wx.GBPosition(7, 0), wx.GBSpan(1, 1),
                        wx.TOP | wx.RIGHT | wx.LEFT, 15)
        
        self.gbSizer2_panel.SetSizer(gbSizer2)
        
        gbSizer_right = wx.GridBagSizer(0, 0)
        gbSizer_right.Add(self.gbSizer2_panel, wx.GBPosition(0, 0), wx.GBSpan(1, 1),
                            wx.EXPAND, 0)
        '''gbSizer_right.Add(self.edit_panel, wx.GBPosition(1, 0), wx.GBSpan(1, 1),
                            wx.EXPAND, 0)
        self.edit_panel.Hide()'''
        

        self.m_panel26.SetSizer(gbSizer_right)

        self.m_panel26.Layout()
        
        gbSizer1.Add(self.m_panel26, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.ALL, 0)
        
        
        
        

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        gbSizer1.AddGrowableRow(0)
        gbSizer1.AddGrowableCol(1)

        gbSizer2.AddGrowableRow(7)
        gbSizer2.AddGrowableCol(3)

        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔为1秒

        # Connect Events
        self.calendar_button.Bind(wx.EVT_BUTTON, self.on_calendar_button)
        self.m_searchCtrl1.Bind(wx.EVT_TEXT, self.on_search)
        self.m_searchCtrl1.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.on_search_cancel)
        self.m_searchCtrl1.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.on_search_search)
        self.m_button1.Bind(wx.EVT_BUTTON, self.new_paper)
        self.m_button11.Bind(wx.EVT_BUTTON, self.new_book)
        self.m_button111.Bind(wx.EVT_BUTTON, self.new_note)
        self.nearly_open_button_more.Bind(wx.EVT_BUTTON, self.open_nearly_data_more)
        self.nearly_open_button.Bind(wx.EVT_BUTTON, self.open_nearly_data)
        self.nearly_open_button2.Bind(wx.EVT_BUTTON, self.open_nearly_data)
        self.nearly_open_button3.Bind(wx.EVT_BUTTON, self.open_nearly_data)
        self.nearly_open_button4.Bind(wx.EVT_BUTTON, self.open_nearly_data)
        self.help_button.Bind(wx.EVT_BUTTON, self.help)
        self.note_list.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.edit_note)
        self.note_list.Bind(wx.EVT_TREE_END_LABEL_EDIT, self.edit_note_end)
        self.m_panel10.Bind(wx.EVT_RIGHT_DOWN, self.show_menu)
        self.note_list.Bind(wx.EVT_RIGHT_DOWN, self.show_menu)
        self.Bind(wx.EVT_MENU, self.menuHandler)
        
        self.note_list.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.open_note)
        self.Bind(wx.EVT_CLOSE, self.on_close)




        
        

       
        self.Bind(wx.EVT_CHAR_HOOK, self.on_key_down)
        
        
        #当窗口大小改变时，更新大小
        '''self.edit_panel.Bind(wx.EVT_SIZE, self.on_size)'''

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def on_timer(self, event):
        event.Skip()
    def clock(self, event):
        event.Skip()

    def on_calendar_button(self, event):
        event.Skip()

    def on_search_search(self, event):
        event.Skip()

    def on_search_cancel(self, event):
        event.Skip()

    def on_search(self, event):
        event.Skip()

    def address_on_enter_window(self, event):
        event.Skip()

    def address_on_leave_window(self, event):
        event.Skip()

    def open_nearly_data_more(self, event):
        event.Skip()

    def open_nearly_data(self, event):
        event.Skip()
    
    def on_size(self, event):
        event.Skip()

    def on_key_down(self, event):
        event.Skip()

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
        event.Skip()

    def edit_note_end(self, event):
        event.Skip()

    def new_paper(self, event):
        event.Skip()

    def new_book(self, event):
        event.Skip()

    def new_note(self, event):
        event.Skip()

    def on_enter_window(self, event):
        event.Skip()

    def on_leave_window(self, event):
        event.Skip()

    def help(self, event=None):
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
