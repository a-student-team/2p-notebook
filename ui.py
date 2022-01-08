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


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"NoteBook", pos=wx.DefaultPosition, size=wx.Size(
            1000, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT,
                     wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.SetMinSize(wx.Size(600, 400))

        menubar = wx.MenuBar(0)
        fileMenu = wx.Menu()
        newMenu = wx.Menu()
        newMenu.Append(
            wx.ID_NEW, u"新建笔记", wx.EmptyString, wx.ITEM_NORMAL)
        newMenu.Append(
            wx.ID_FILE, u"新建笔记本", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(wx.ID_ANY, u"新建", newMenu)
        fileMenu.AppendSeparator()
        fileMenu.Append(
            wx.ID_OPEN, u"打开", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.AppendSeparator()
        fileMenu.Append(
            wx.ID_SAVE, u"保存", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.Append(
            wx.ID_SAVEAS, u"另存为", wx.EmptyString, wx.ITEM_NORMAL)
        fileMenu.AppendSeparator()
        fileMenu.Append(
            wx.ID_EXIT, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        menubar.Append(fileMenu, u"文件")
        
        self.SetMenuBar(menubar)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel10 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 700), wx.TAB_TRAVERSAL)
        self.m_panel10.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.m_panel10.SetMinSize(wx.Size(200, 500))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer5.SetMinSize(wx.Size(200, 500))
        self.m_staticText9 = wx.StaticText(
            self.m_panel10, wx.ID_ANY, u"我的笔记", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(wx.Font(
            24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.m_staticText9.SetForegroundColour(wx.Colour(247, 247, 247))

        bSizer5.Add(self.m_staticText9, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.note_list = wx.TreeCtrl(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, 700), wx.TR_FULL_ROW_HIGHLIGHT |
                                     wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT | wx.TR_NO_LINES | wx.BORDER_NONE | wx.WANTS_CHARS | wx.TR_SINGLE | wx.EXPAND | wx.HSCROLL)
        self.note_list.SetForegroundColour(wx.Colour(247, 247, 247))
        self.note_list.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))
        self.note_list.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        bSizer5.Add(self.note_list, 0, wx.ALL, 5)

        self.m_panel10.SetSizer(bSizer5)
        self.m_panel10.Layout()
        gbSizer1.Add(self.m_panel10, wx.GBPosition(0, 0),
                     wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)

        self.m_panel26 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(700, 700), wx.TAB_TRAVERSAL)
        self.m_panel26.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.morning_night = wx.StaticText(
            self.m_panel26, wx.ID_ANY, u"早上好", wx.DefaultPosition, wx.DefaultSize, 0)
        self.morning_night.Wrap(-1)

        self.morning_night.SetFont(wx.Font(
            75, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.morning_night.SetForegroundColour(wx.Colour(BLACK))

        gbSizer2.Add(self.morning_night, wx.GBPosition(
            0, 0), wx.GBSpan(1, 2), wx.ALL, 10)

        self.time_text = wx.StaticText(
            self.m_panel26, wx.ID_ANY, u"time", wx.DefaultPosition, wx.DefaultSize, 0)
        self.time_text.Wrap(-1)

        self.time_text.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.time_text.SetForegroundColour(wx.Colour(BLACK))

        gbSizer2.Add(self.time_text, wx.GBPosition(0, 2),
                     wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.m_button1 = wx.Button(self.m_panel26, wx.ID_ANY, u"添加新的笔记", wx.DefaultPosition,
                                   wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE | wx.BORDER_THEME)

        self.m_button1.SetBitmapFocus(wx.NullBitmap)
        self.m_button1.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button1, wx.GBPosition(1, 0),
                     wx.GBSpan(1, 1), wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button11 = wx.Button(self.m_panel26, wx.ID_ANY, u"添加新的笔记本", wx.DefaultPosition,
                                    wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE | wx.BORDER_THEME)
        self.m_button11.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button11, wx.GBPosition(2, 0),
                     wx.GBSpan(1, 1), wx.TOP | wx.RIGHT | wx.LEFT, 15)

        self.m_button111 = wx.Button(self.m_panel26, wx.ID_ANY, u"添加新的便签", wx.DefaultPosition,
                                     wx.DefaultSize, wx.BORDER_NONE | wx.BORDER_NONE | wx.BORDER_SIMPLE | wx.BORDER_THEME)
        self.m_button111.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))

        gbSizer2.Add(self.m_button111, wx.GBPosition(
            3, 0), wx.GBSpan(1, 1), wx.ALL, 15)

        self.m_panel26.SetSizer(gbSizer2)

        self.m_panel26.Layout()
        gbSizer1.Add(self.m_panel26, wx.GBPosition(0, 1),
                     wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 0)

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

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
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
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, size=wx.DefaultSize, pos=wx.DefaultPosition,):
        # import ./hmtl/edit.html and show
        # use html2
        
        wx.Frame.__init__(self, parent, id=id, title=title, size=size,
                          pos=pos, style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)


class NoBorderFrame(wx.Frame):
    # a frame that has a sizer without borders
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER, name=wx.FrameNameStr):
        wx.Frame.__init__(self, parent, id=id, title=title,
                          size=size, pos=pos, style=style, name=name)

        self.Center()
        self.Show(True)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        # a sizer like windows title bar
        self.sizer = wx.GridSizer(0, 0, 0, 0)

        # close button
        self.close_bitmap = wx.Bitmap(
            get_file('\\images\\close.png'), wx.BITMAP_TYPE_PNG)

        self.close_button = wx.BitmapButton(self, wx.ID_ANY, self.close_bitmap, style=wx.BU_AUTODRAW | wx.BORDER_NONE | wx.BU_RIGHT, size=(
            self.close_bitmap.GetWidth()+5, self.close_bitmap.GetHeight()+5))
        # set background color like frame
        self.close_button.SetBackgroundColour(self.GetBackgroundColour())
        self.close_button.SetBitmapFocus(
            wx.Bitmap(get_file('\\images\\close_focus.png'), wx.BITMAP_TYPE_PNG))

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


class FastNote (NoBorderFrame):  # 便签

    def __init__(self, parent):
        NoBorderFrame.__init__(self, parent, id=wx.ID_ANY,
                               pos=wx.DefaultPosition, size=wx.Size(200, 200))

    def print_screen(self):

        self.m_textCtrl2 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_MULTILINE)
        self.m_textCtrl2.SetFont(wx.Font(
            18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
        self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))

        self.main_sizer.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(self.main_sizer)

        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class MyApp(wx.App):
    def OnInit(self):
        FastNote(None).Show()

        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
