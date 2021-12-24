import wx
import time

from wx import html2

from ui import MyFrame1, EditFrame1, FastNote
import os


def get_file(file_name):
    '''
    :param file_name: relative file path, like '\\data\\test.txt'
    :return: file path
    '''
    return os.path.dirname(os.path.abspath(__file__)) + file_name


class MainFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.root = self.note_list.AddRoot("所有笔记")
        self.root_note = []  # list of book name

        self.note_list.ExpandAll()  # ?

        # the data for local file
        # the data for write to local file, like {'book':{'note':'content'}}
        self.note_local_data = {}

    def _change_note_local_data(self):
        # change the note_local_data
        for book in self.root_note:
            self.note_local_data[book] = {}
            for child in self.note_list.GetChildren(self.note_list.GetRootItem()):
                if self.note_list.GetItemText(child) == book:
                    for note in self.note_list.GetChildren(child):
                        self.note_local_data[book][self.note_list.GetItemText(
                            note)] = self.note_list.GetItemText(note, 1)

    def new_paper(self, event):
        # get selected item and append new item in it
        root = self.note_list.GetSelection()
        # if root is paper, root = root.parent
        if self.note_list.GetItemParent(root) != self.root:
            root = self.note_list.GetItemParent(root)
        try:

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

        self.note_list.AppendItem(root, name)
        self.note_list.Expand(root)
        self.note_list.ExpandAll()

    def new_book(self, event):

        name = CreateDialog(self, "新笔记本").m_textCtrl1.GetValue()

        if name == '':
            return None

        book = self.note_list.AppendItem(self.root, name)
        self.note_list.Expand(book)
        self.note_list.ExpandAll()
        self.root_note.append(name)

        print(self.root_note, self.note_list)

    def new_note(self, event):
        FastNote(self).Show()

    def show_menu(self, event):
        menu = wx.Menu()
        create_menu = wx.Menu()
        create_note = create_menu.Append(wx.ID_NEW, '新建笔记')
        create_book = create_menu.Append(wx.ID_FILE, '新建笔记本')
        menu.AppendSubMenu(create_menu, '新建')
        menu.Append(wx.ID_REFRESH, "重命名", '重命名')
        menu.Append(wx.ID_DELETE, "删除", '删除')

        self.PopupMenu(menu)

        menu.Destroy()
        return super().show_menu(event)

    def menuHandler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            self.new_paper(event)
        elif id == wx.ID_REFRESH:
            self.rename_paper(event)
        elif id == wx.ID_DELETE:
            self.delete_paper(event)
        elif id == wx.ID_FILE:
            self.new_book(event)
        else:
            event.Skip()

    def rename_paper(self, event):
        root = self.note_list.GetSelection()
        name = CreateDialog(self).m_textCtrl1.GetValue()
        if name == '':
            return None
        self.note_list.SetItemText(root, name)

    def delete_paper(self, event):
        root = self.note_list.GetSelection()
        self.note_list.Delete(root)

    def change_time(self, event):
        self.time_text.SetLabel(
            "时间:"+str(time.strftime('%Y-%m-%d %H:%M:%S')))

        mytime = time.localtime()
        self.morning_night.SetLabel("晚上好" if 18 < mytime.tm_hour < 23 else (
            "上午好" if 0 < mytime.tm_hour < 12 else "下午好"))

    def open_note(self, event):
        # use EditFrame
        # if item's parent is root , don't open it

        root = self.note_list.GetSelection()
        if self.note_list.GetItemParent(root) == self.root:
            return None
        else:
            edit_browser = EditFrame(self, title="编辑笔记", size=(800, 600), paper_title=self.note_list.GetItemText(root))
            edit_browser.browser.LoadURL(get_file('\\html\\edit.html'))
            edit_browser.Show()


class EditFrame(EditFrame1):
    # function for edit note
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, size=wx.DefaultSize, pos=wx.DefaultPosition, paper_title = "title"):
        EditFrame1.__init__(self, parent, id, title, size, pos)
        self.paper_title = paper_title
        self.Bind(html2.EVT_WEBVIEW_LOADED, self.OnPageLoaded,
                  self.browser)
        
    def OnPageLoaded(self, event):
        # set title to edit
        self.browser.RunScript(
            "document.getElementById('file_name').value = '"+self.paper_title+"'")
        event.Skip()


class CreateDialog (wx.Dialog):  # 名字输入框

    def __init__(self, parent, value=""):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(171, 129), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(100, 120), wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"请输入名字:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, str(value), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_button5.Bind(wx.EVT_BUTTON, self.note_name)
        self.Bind(wx.EVT_CLOSE, self.close)

        self.ShowModal()

    def note_name(self, event):
        self.Destroy()

    def __del__(self):
        pass

    def close(self, event):
        self.m_textCtrl1.SetValue("")
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
