import os
import time
import wx
from NoBorderFrame import NoBorderFrame
from get_file import get_file
from wx.richtext import RichTextCtrl
class FastNote(NoBorderFrame):  # 便签

    def __init__(self, parent):
        
        NoBorderFrame.__init__(self,
                               parent,
                               id=wx.ID_ANY,
                               pos=wx.DefaultPosition,
                               size=wx.Size(200, 200))
        self.parent = parent
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.Centre(wx.BOTH)
        self.Bind(wx.EVT_CHAR_HOOK , self.OnKeyDown)

    def OnKeyDown(self, event):
        #按下Ctrl+F显示/隐藏self.sizer
        print("key")
        if event.ControlDown() and event.GetKeyCode() == 70:
            if self.main_sizer.IsShown(self.sizer):
                self.main_sizer.Hide(self.sizer)
            else:
                self.main_sizer.Show(self.sizer)
            self.main_sizer.Layout()
        else:
            event.Skip()

    def print_title_sizer(self):
        self.font_size_btn = wx.Button(self,
                                        wx.ID_ANY,
                                        'A',
                                        size=(30, 30),
                                        style=wx.BORDER_NONE | wx.BORDER_SIMPLE)
        self.font_size_btn.SetBackgroundColour(self.GetBackgroundColour())
        self.font_size_btn.Bind(wx.EVT_ENTER_WINDOW, self.font_btn_enter_window)
        self.font_size_btn.Bind(wx.EVT_LEAVE_WINDOW, self.font_btn_leave_window)

        self.more_bitmap = wx.Bitmap(get_file('\\images\\more.png'),
                                        wx.BITMAP_TYPE_PNG)
        
        self.more_button = wx.BitmapButton(
            self,
            wx.ID_ANY,
            self.more_bitmap,
            style=wx.BU_AUTODRAW | wx.BORDER_NONE | wx.BU_RIGHT,
            size=(30, 30))
        self.more_button.SetBackgroundColour(self.GetBackgroundColour())
        self.more_button.Bind(wx.EVT_ENTER_WINDOW, lambda event:self.btn_enter_window(event, (225, 225, 225)))
        self.more_button.Bind(wx.EVT_LEAVE_WINDOW, self.btn_leave_window)
        self.more_button.Bind(wx.EVT_BUTTON, self.OnMore)
        self.sizer.Add(self.more_button, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.sizer.Add(self.font_size_btn, 0, wx.ALL | wx.ALIGN_LEFT, 0)
        self.font_size_btn.Bind(wx.EVT_BUTTON, self.OnFontSize)
    def font_btn_leave_window(self, event):
        self.font_size_btn.SetBackgroundColour(self.GetBackgroundColour())
        self.font_size_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.font_size_btn.Refresh()
        event.Skip()
    def font_btn_enter_window(self, event):
        self.font_size_btn.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.font_size_btn.SetForegroundColour(wx.Colour(0, 0, 0))
        self.font_size_btn.Refresh()
        event.Skip()

    def OnMore(self, event):
        # 更多功能: 另存为本地文件, 当做笔记存入笔记本, 是否置顶
        def save_as(data):
            dialog = wx.FileDialog(self,
                                      message="另存为...",
                                      defaultDir=os.getcwd(),
                                      defaultFile="",
                                      wildcard="*.txt",
                                      style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dialog.ShowModal() == wx.ID_OK:
                try:
                    path = dialog.GetPath()
                    with open(path, 'w') as f:
                        f.write(data)
                except:
                    wx.MessageBox("保存失败", "错误", wx.OK | wx.ICON_ERROR)
            dialog.Destroy()

        #提供三个选项给用户选择
        if self.GetWindowStyleFlag() & wx.STAY_ON_TOP:
            self.more_dialog = wx.SingleChoiceDialog(self,
                                                        "请选择操作",
                                                        "更多",
                                                        ["另存为本地文件", "当做笔记存入笔记本", "取消置顶", "更改为专注模式"],
                                                        wx.CHOICEDLG_STYLE|wx.RESIZE_BORDER)
        else:
            self.more_dialog = wx.SingleChoiceDialog(self,
                                                        "请选择操作",
                                                        "更多",
                                                        ["另存为本地文件", "当做笔记存入笔记本", "置顶", "更改为专注模式"],
                                                        wx.CHOICEDLG_STYLE|wx.RESIZE_BORDER)
        if self.more_dialog.ShowModal() == wx.ID_OK:
            if self.more_dialog.GetStringSelection() == "另存为本地文件":
                save_as(self.m_textCtrl2.GetValue())
            elif self.more_dialog.GetStringSelection() == "当做笔记存入笔记本":
                note_data = self.parent.note_data
                time_ = time.strftime("%m-%d %H:%M", time.localtime())
                if note_data.get("便签") != None:
                    

                    if note_data["便签"].get(time_+"的记录") != None:
                        note_data["便签"][time_+"的记录"].append(self.m_textCtrl2.GetValue())
                    else:
                        #notice user a dialog
                        dialog = wx.MessageDialog(self,
                                                    "发现有相同名字的笔记, 是否覆盖?",
                                                    "提示",
                                                    wx.YES_NO | wx.ICON_QUESTION)
                        if dialog.ShowModal() == wx.ID_YES:
                            note_data["便签"][time+"的记录"] = self.m_textCtrl2.GetValue()
                        else:
                            #提醒用户重试
                            dialog = wx.MessageDialog(self,
                                                        "请重试",
                                                        "提示",
                                                        wx.OK | wx.ICON_INFORMATION)
                            dialog.ShowModal()
                            dialog.Destroy()
                else:
                    note_data["便签"] = {"type": "0"}
                    note_data["便签"][time_+"的记录"] = self.m_textCtrl2.GetValue()
                self.parent.note_data = note_data
                self.parent.refresh_note_list_from_note_data()

            elif self.more_dialog.GetStringSelection() == "置顶":
                self.SetWindowStyle(wx.STAY_ON_TOP)
            elif self.more_dialog.GetStringSelection() == "取消置顶":
                self.SetWindowStyle(self.GetWindowStyle()^wx.STAY_ON_TOP)

            elif self.more_dialog.GetStringSelection() == "更改为专注模式":
                self.main_sizer.Hide(self.sizer)
                #提醒用户Ctrl+F键显示sizer
                dialog = wx.MessageDialog(self,
                                            "按Ctrl+F键更改为专注模式/普通模式",
                                            "提示",
                                            wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                dialog.Destroy()
                self.main_sizer.Layout()
                
        self.more_dialog.Destroy()

    def OnFontSize(self, event):
        #修改字体大小
        
        font_size = wx.GetNumberFromUser('输入字体大小', '字体大小', '字体大小',
                                            self.m_textCtrl2.GetFont().GetPointSize(),
                                            1,
                                            100)
        if font_size > 0:
            self.m_textCtrl2.SetFont(wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                                wx.FONTSTYLE_NORMAL,
                                                wx.FONTWEIGHT_NORMAL, False,
                                                "Microsoft YaHei UI"))
            self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))
            self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
            self.m_textCtrl2.SetValue(self.m_textCtrl2.GetValue())
            self.m_textCtrl2.Refresh()
            self.Layout()

        

    def print_screen(self):

        self.m_textCtrl2 = RichTextCtrl(self,
                                       wx.ID_ANY,
                                       wx.EmptyString,
                                       wx.DefaultPosition,
                                       wx.DefaultSize,
                                       style=wx.NO_BORDER|wx.TE_MULTILINE)
        
        self.m_textCtrl2.SetFont(
            wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                    wx.FONTWEIGHT_NORMAL, False, "Microsoft YaHei UI"))
        
        self.m_textCtrl2.SetBackgroundColour(self.GetBackgroundColour())
        self.m_textCtrl2.SetForegroundColour(wx.Colour(0, 0, 0))

        self.main_sizer.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(self.main_sizer)

        self.Layout()

    def __del__(self):
        pass

#test
if __name__ == '__main__':
    app = wx.App()
    frame = FastNote(None)
    frame.Show()
    app.MainLoop()

