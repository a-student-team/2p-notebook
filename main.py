import wx
from wx import html2

from ui import MyFrame1, EditFrame1, FastNote

import os
import uuid
import random
import time


def random_str(num=6):
    uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
    a = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
    b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串 与 uuid拼接
    return b  # 返回随机字符串


def get_file(file_name):
    '''
    :param file_name: relative file path, like '\\data\\test.txt'
    :return: file path
    '''
    return os.path.dirname(os.path.abspath(__file__)) + file_name


class Paper(object):

    def __init__(self, title="标题", content="内容"):
        self.title = title
        self.content = content
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.uuid = random_str()

    def __repr__(self):
        return '<Paper title: %s, content: %s, time: %s, uuid: %s>' % (
            self.title, self.content, self.time, self.uuid)


class MainFrame(MyFrame1):

    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.root = self.note_list.AddRoot("所有笔记")
        self.books = {}  # dict of book name
        self.note_list.ExpandAll()
        self.file_path = []  # list of file_path, like{"path1", "path2", ...}
        self.nearlyfile = [
            self.file1, self.file2, self.file3, self.file4, self.file5
        ]

        # the data like {'book':{'note':'content',...},...}
        self.note_data = {}

        #import data
        if self.get_note_data_in_file() == False:
            #create a new main.note file
            self.write_note_data_to_file()
        if self.get_data_in_file() == False:
            #create a new main.data file
            self.write_data_to_file()

        self.note_list.DeleteAllItems()
        self.note_list.AddRoot("所有笔记")
        for book in self.note_data:
            book_item = self.note_list.AppendItem(self.note_list.GetRootItem(),
                                                  book)
            for note in self.note_data[book]:
                self.note_list.AppendItem(book_item, note)
        self.note_list.ExpandAll()

    def _note_in_note_data(self, note):
        # check if note in note_data
        for book in self.note_data:
            if note in self.note_data[book]:
                return True
        return False

    def _book_in_note_data(self, book):
        # check if book in note_data
        if book in self.note_data:
            return True
        return False

    def _updata_note_data(self):
        # update data
        pass

    def _update_nearlyfileMenu(self):
        # update nearlyfileMenu
        for i in range(5):
            try:
                self.nearlyfile[i].SetItemLabel(self.file_path[i])
            except:
                self.nearlyfile[i].SetItemLabel(" ")

    def write_data_to_file(self):
        #write data to file
        with open(get_file('\\data\\main.data'), 'w', encoding="utf-8") as f:
            try:
                f.write(str(self.nearlyfile))
                return True
            except:
                return False

    def get_data_in_file(self):
        #get data in file
        with open(get_file("\\data\\main.data"), "r", encoding="utf-8") as f:
            try:
                data = eval(f.read())
                self.nearlyfile = data
                return True
            except:
                return False

    def write_note_data_to_file(self, file_path=get_file('\\data\\main.note')):
        #write note_data to local file
        '''
        param file_name: relative file path, like 'test.note'
        '''
        # self._updata_note_data()
        print(file_path)

        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(str(self.note_data))

    def get_note_data_in_file(self, file_path=get_file('\\data\\main.note')):

        if file_path == get_file('\\data\\main.note'):
            # main.note file exist
            if not os.path.exists(file_path):
                return False
            # make a list about note local files,use os.listdir to get all files in the dir
            importlist = os.listdir(
                os.path.dirname(os.path.abspath(__file__)) + '\\data')
            #read note data from local files
            for file in importlist:
                if file.endswith('.note'):
                    with open(os.path.dirname(os.path.abspath(__file__)) +
                              '\\data\\' + file,
                              'r',
                              encoding="utf-8") as f:

                        try:
                            self.note_data.update(eval(f.read()))
                        except:
                            pass

            return True
        # read note_data from local file
        with open(file_path, 'r', encoding="utf-8") as f:

            try:
                note_data_temp = eval(f.read())

                if self._dic_in_note_data(note_data_temp):
                    #notice user to choose yes or no

                    dialog = wx.MessageDialog(self,
                                              '发现有重名的文件, 将会合并(或删除), 是否继续导入?',
                                              '提示',
                                              wx.OK | wx.ICON_INFORMATION)

                    if dialog.ShowModal() == wx.ID_NO:
                        dialog.Destroy()
                        return None

                    dialog.Destroy()
                #add note_data_temp to self.note_data
                self.note_data.update(note_data_temp)
                return True
            except:

                return False

    def _dic_in_note_data(self, dic):
        # if dic in note_data, return True, else False
        for i in dic:
            if i in self.note_data:

                return True
            print(i)

        return False

    def new_paper(self, event):
        # get selected item and append new item in it
        root = self.note_list.GetSelection()
        print(root)

        try:
            # if root is paper, root = root.parent
            if self.note_list.GetItemParent(root) != self.root:
                root = self.note_list.GetItemParent(root)

            self.note_list.Expand(root)
            self.note_list.ExpandAll()
        except:
            dialog = wx.MessageDialog(self, '请选择笔记本', '提示',
                                      wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None

        name = CreateDialog(self, "新笔记").m_textCtrl1.GetValue()

        if name == '':
            return None

        if self._note_in_note_data(name):
            dialog = wx.MessageDialog(self, '名字重复啦, 笔记已存在', '提示',
                                      wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None
        print(self.note_data[self.note_list.GetItemText(root)])

        self.note_list.AppendItem(root, name)

        self.note_list.Expand(root)
        self.note_list.ExpandAll()

        self.note_data[self.note_list.GetItemText(root)][name] = '内容'

    def new_book(self, event):

        name = CreateDialog(self, "新笔记本").m_textCtrl1.GetValue()

        if name == '':
            return None
        if self._book_in_note_data(name):
            dialog = wx.MessageDialog(self, '名字重复啦, 笔记本已存在', '提示',
                                      wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None

        book = self.note_list.AppendItem(self.root, name)
        self.note_list.Expand(book)
        self.note_list.ExpandAll()
        self.books[name] = book
        self.note_data[name] = {}
        print(self.books, self.note_list)

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
        elif id == wx.ID_EXIT:
            self.Close()
        elif id == wx.ID_OPEN:
            self.open(event)
        elif id == wx.ID_SAVE:
            self.save(event)
        elif id == wx.ID_SAVEAS:
            self.save_as(event)
        elif id == wx.ID_FILE1:
            self.get_note_data_in_file(self.file1.GetLabelText())
        elif id == wx.ID_FILE2:
            self.get_note_data_in_file(self.file2.GetLabelText())
        elif id == wx.ID_FILE3:
            self.get_note_data_in_file(self.file3.GetLabelText())
        elif id == wx.ID_FILE4:
            self.get_note_data_in_file(self.file4.GetLabelText())
        elif id == wx.ID_FILE5:
            self.get_note_data_in_file(self.file5.GetLabelText())
        else:
            event.Skip()

    def save_as(self, event):
        # use file dialog(only xxx.note) to get file name, and save data
        # if save successfully, show a dialog for user
        # dialog's default path is get_file("\\data")
        # and save the path in self.file_path
        dialog = wx.FileDialog(self,
                               message="保存文件",
                               defaultDir=get_file("\\data"),
                               defaultFile="",
                               wildcard="*.note",
                               style=wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            if self.write_note_data_to_file(file_path) == False:
                dialog = wx.MessageDialog(self, '保存失败', '提示',
                                          wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                dialog.Destroy()
                return None
        if file_path not in self.file_path:
            self.file_path.append(file_path)
        self._update_nearlyfileMenu()

        dialog.Destroy()

    def save(self, event):
        self.write_note_data_to_file()
        dialog = wx.MessageDialog(self, '保存成功', '提示',
                                  wx.OK | wx.ICON_INFORMATION)
        dialog.ShowModal()
        dialog.Destroy()

    def open(self, event):
        # open xxx.note in local file, use file dialog
        dlg = wx.FileDialog(self, "选择文件", os.getcwd(), "", "*.note",
                            wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()
            get = self.get_note_data_in_file(str(file_path))
            if get == False:
                #show a dialog to user
                print(file_path)
                dialog = wx.MessageDialog(self, '文件导入失败', '提示',
                                          wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                dialog.Destroy()
                return None
            elif get == None:
                return None
            if file_path not in self.file_path:
                self.file_path.append(file_path)
            self._update_nearlyfileMenu()
            self.note_list.DeleteAllItems()
            self.note_list.AddRoot("所有笔记")
            for book in self.note_data:
                book_item = self.note_list.AppendItem(
                    self.note_list.GetRootItem(), book)
                for note in self.note_data[book]:
                    self.note_list.AppendItem(book_item, note)
            self.note_list.ExpandAll()
            #self.note_list.Expand(self.root)

        dlg.Destroy()

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
        self.time_text.SetLabel("时间:" +
                                str(time.strftime('%Y-%m-%d %H:%M:%S')))

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
            edit_browser = EditFrame(
                self,
                title="编辑笔记",
                size=(800, 600),
                paper_title=self.note_list.GetItemText(root))

            text = self.note_data[self.note_list.GetItemText(
                self.note_list.GetItemParent(root))][
                    self.note_list.GetItemText(root)]
            edit_browser.browser.LoadURL(
                get_file('\\html\\edit.html?text={}'.format(text)))
            edit_browser.Show()
            edit_browser.Bind(
                wx.EVT_CLOSE,
                lambda event: self.edit_browser_close(event, root))
            # when it open, give a value to edit_browser.browser
            edit_browser.Bind(
                html2.EVT_WEBVIEW_LOADED,
                lambda event: self.edit_browser_open(event, root))

    def edit_browser_open(self, event, root=None):
        pass

    def edit_browser_close(self, event, root=None):
        #ask user save or not
        # if save, use html2.runScript the function getText() to get text and save it into note_data
        if root == None:
            root = self.note_list.GetSelection()
        if self.note_list.GetItemParent(root) == self.root:
            return None
        else:
            edit_browser = event.GetEventObject()
            text = edit_browser.browser.RunScript("getText()")
            self.note_data[self.note_list.GetItemText(
                self.note_list.GetItemParent(root))][
                    self.note_list.GetItemText(root)] = text[1]
            edit_browser.Destroy()
            self.note_list.ExpandAll()

    def on_close(self, event):
        # ask user save or not
        # if save, use funcion save()
        dialog = wx.MessageDialog(self, '是否保存笔记', '提示',
                                  wx.YES_NO | wx.ICON_INFORMATION)
        if dialog.ShowModal() == wx.ID_YES:
            self.save(None)
        dialog.Destroy()
        self.Destroy()

    def __del__(self):
        pass


class EditFrame(EditFrame1):
    # function for edit note
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

    def OnPageLoaded(self, event):
        event.Skip()


class CreateDialog(wx.Dialog):  # 名字输入框

    def __init__(self, parent, value=""):
        wx.Dialog.__init__(self,
                           parent,
                           id=wx.ID_ANY,
                           title=wx.EmptyString,
                           pos=wx.DefaultPosition,
                           size=wx.Size(171, 129),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(100, 120), wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"请输入名字:",
                                           wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)

        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, str(value),
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
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
