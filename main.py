import wx
from wx import html2

from ui import MyFrame1
from get_file import get_file
from EditFrame import EditFrame
from CreateDialog import CreateDialog
from FastNote import FastNote
from SettingFrame import SettingFrame
from encryption import encrypt, decrypt
from EncryptDialog import EncryptDialog
from HelpFrame import HelpFrame
import os
import uuid
import random
import time
import json


class MainFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.root = self.note_list.AddRoot("所有笔记")
        self.books = {}  # dict of book name
        self.note_list.ExpandAll()  
        self.file_path = [] # list of file_path, like{"path1", "path2", ...}
        self.nearlyfile = [self.file1, self.file2, self.file3, self.file4, self.file5]
        self._note_list_is_changed = False
        self.edit_count = 0 #喵的我真的不会写了QAQ,如果把这个删了刚打开就会提示没保存
        # the data like {'book':{'type':'1','note':'content',...},...}
        self.note_data = {}
        self.key = {} #eg. {'note':'key',...}
        
        
        
        #import data
        if self.get_note_data_in_file() == False:
            #create a new main.note file
            self.write_note_data_to_file()
        if self.get_data_in_file() == False:
            #create a new main.data file
            print("create a new main.data file")
            self.write_data_to_file()
        
        
        self.note_list.DeleteAllItems()
        self.note_list.AddRoot("所有笔记")
        
        for book in self.note_data:
            if book.find("NgsAABwEVA==")!= -1:
                print(book)
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book[12:]) 
                
            else:
                print(book)
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
            for t, note in self.note_data[book].items():
                print(t, note)
                if t == "type":
                    continue
                self.note_list.AppendItem(book_item, t)
            
        self.note_list.ExpandAll()
        
   
    def sort_note_list(self):
        # sort note list
        self.note_list.SortChildren(self.note_list.GetRootItem())

    def note_list_is_changed(self, event=None):
        if self.edit_count != 0:
            self._note_list_is_changed = True
            #set win topic a "*"
            self.Title = "*" + self.Title if self.Title[0] != "*" else self.Title
            
        self.edit_count += 1

    def _note_in_note_data(self, note, root=None):
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
        try:
            with open(get_file('\\data\\main.data'), 'w', encoding="utf-8") as f:
                
                f.write(str(self.file_path))
                return True
        except:
            return False
    def get_data_in_file(self):
        #get data in file
        try:
            with open(get_file("\\data\\main.data"), "r", encoding="utf-8") as f:
                
                data = eval(f.read())
                self.file_path = data
                self._update_nearlyfileMenu()
                return True
        except:
            return False
            
            
    def write_note_data_to_file(self, file_path=get_file('\\data\\note\\main.note')):
        #write note_data to local file
        '''
        param file_name: relative file path, like 'test.note'
        '''
        # self._updata_note_data()
        print(file_path)
        
        
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(str(self.note_data))
    
    def get_note_data_in_file(self, file_path=get_file('\\data\\note\\main.note')):
        
        if file_path == get_file('\\data\\note\\main.note'):
            print(file_path)
            # main.note file exist
            if not os.path.exists(file_path):
                
                return False
            # make a list about note local files,use os.listdir to get all files in the dir
            importlist = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '\\data\\note\\')
            #read note data from local files
            for file in importlist:
                if file.endswith('.note'):
                    with open(os.path.dirname(os.path.abspath(__file__)) + '\\data\\note\\' + file, 'r', encoding="utf-8") as f:
                        
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
                    
                    dialog = wx.MessageDialog(
                self, '发现有重名的文件, 将会合并(或删除), 是否继续导入?', '提示', wx.OK | wx.ICON_INFORMATION)
                    
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
        
        self.note_list_is_changed()

        self.sort_note_list()

        try:
            self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(root)][name] = '内容'
        except:
            self.note_data[self.note_list.GetItemText(root)][name] = '内容'


    def new_book(self, event):

        dialog = CreateDialog(self, "新笔记本", True)
        name = str(dialog.m_textCtrl1.GetValue())
        if self._book_in_note_data(name) or self._book_in_note_data("NgsAABwEVA=="+name):
            dialog = wx.MessageDialog(
                self, '名字重复啦, 笔记本已存在', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None
        if name == '':
            return None
        if dialog.m_checkBox1.GetValue():
            
            e_dialog = EncryptDialog(self)
            e_dialog.ShowModal()
            key = e_dialog.m_textCtrl1.GetValue()
            book = self.note_list.AppendItem(self.note_list.GetRootItem(), name, image=0)
            book = self.note_list.FindItem(self.note_list.GetRootItem(), name)
            #添加本地图标icon.ico
            

            
            self.note_list.Expand(self.note_list.GetRootItem())
            self.note_list.ExpandAll()

            self.key[self.note_list.GetItemText(self.note_list.GetSelection())]= key
            self.note_data["NgsAABwEVA=="+name] = {"type":1}
        else:

            book = self.note_list.AppendItem(self.note_list.GetRootItem(), name)
            
            self.note_list.Expand(self.note_list.GetRootItem())
            self.note_list.ExpandAll()
            self.books[name] = book
            self.note_data[name] = {"type":0}
            
        print(self.books, self.note_list)
        self.sort_note_list()

        self.note_list_is_changed()
        

        
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
        elif id == self.ID_THEME_DEFAULT:
            self.set_theme(get_file("\\data\\theme\\default.theme.json"))
        elif id == self.ID_THEME_DARK:
            self.set_theme(get_file("\\data\\theme\\dark.theme.json"))
        elif id == self.ID_THEME_LIGHT:
            self.set_theme(get_file("\\data\\theme\\light.theme.json"))
        elif id == self.ID_THEME_OTHER:
            self.edit_theme()
        elif id == wx.ID_HELP:
            self.help()
        else:
            event.Skip()

    def help(self):
        frame = HelpFrame(self)
        frame.Show()

    def save_as(self, event):
        # use file dialog(only xxx.note) to get file name, and save data
        # if save successfully, show a dialog for user
        # dialog's default path is get_file("\\data")
        # and save the path in self.file_path
        dialog = wx.FileDialog(
            self, message="保存文件", defaultDir=get_file("\\data"),
            defaultFile="", wildcard="*.note", style=wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            file_path = dialog.GetPath()
            if self.write_note_data_to_file(file_path) == False:
                dialog = wx.MessageDialog(
                    self, '保存失败', '提示', wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                dialog.Destroy()
                return None
        if file_path not in self.file_path:
            self.file_path.append(file_path)
        self._update_nearlyfileMenu()
        self._note_list_is_changed = False
        
            
        dialog.Destroy()
    def save(self, event):
        self.write_note_data_to_file()
        self._note_list_is_changed = False
        self.Title = self.Title[1:]

    def open(self, event):
        # open xxx.note in local file, use file dialog
        dlg = wx.FileDialog(self, "选择文件", os.getcwd(), "", "*.note", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()
            get = self.get_note_data_in_file(str(file_path))
            if get == False:
                #show a dialog to user
                print(file_path)
                dialog = wx.MessageDialog(
                    self, '文件导入失败', '提示', wx.OK | wx.ICON_INFORMATION)
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
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
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
        try:
            self.note_data[name] = self.note_data.pop(self.note_list.GetItemText(root))
        except:
            #rename self.note_data[parent][name]
            try:
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][name] = self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))
            except:
                try:
                    self.note_data["NgsAABwEVA=="+name] = self.note_data.pop("NgsAABwEVA=="+self.note_list.GetItemText(root))
                except:
                    #rename self.note_data[parent][name]
                    self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(self.note_list.GetItemParent(root))][name] = self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))

        print(self.note_data)
        self.note_list.SetItemText(root, name)
        
        self.note_list_is_changed()

    def delete_paper(self, event):
        root = self.note_list.GetSelection()
        try:
            self.note_data.pop(self.note_list.GetItemText(root))
        except:
            try:
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))
            except:
                try:
                    self.note_data.pop("NgsAABwEVA=="+self.note_list.GetItemText(root))
                except:
                    try:
                        self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))
                    except:
                        #notice user
                        dialog = wx.MessageDialog(
                            self, '删除失败', '提示', wx.OK | wx.ICON_INFORMATION)
                        dialog.ShowModal()
                        dialog.Destroy()
                        
                        return None
        
        self.note_list.Delete(root)
        
        self.note_list_is_changed()

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
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            return None
        if root == self.note_list.GetRootItem():
            return None
        else:
            #全屏
            edit_browser = EditFrame(self, title="编辑笔记", size=wx.Size(wx.GetDisplaySize())
            , paper_title=self.note_list.GetItemText(root))
            try:
                text = self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)]
                #如果加密, 则提醒用户输入密码解密
            
                dialog = EncryptDialog(self, '')
                dialog.ShowModal()
                self._key = str(dialog.m_textCtrl1.GetValue())
                print(text)
                if text != "":
                    text = decrypt(text, self._key)
                else:
                    text = ""
            except:
                text = self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)]
            edit_browser.browser.LoadURL(get_file('\\html\\edit.html?text={}'.format(text)))
            edit_browser.Show()
            edit_browser.Bind(wx.EVT_CLOSE, lambda event: self.edit_browser_close(event, root))
            # when it open, give a value to edit_browser.browser
            edit_browser.Bind(html2.EVT_WEBVIEW_LOADED, lambda event: self.edit_browser_open(event, root))
            
    def edit_browser_open(self, event, root=None):
        pass
        

    def edit_browser_close(self, event, root=None):
        #ask user save or not
        # if save, use html2.runScript the function getText() to get text and save it into note_data
        self.note_list_is_changed()
        if root == None:
            root = self.note_list.GetSelection()
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            return None
        else:
            edit_browser = event.GetEventObject()
            text = edit_browser.browser.RunScript("getText()")
            try:
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)] = text[1]
            except:
                self.note_data["NgsAABwEVA=="+self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)] = encrypt(text[1], self._key)
            edit_browser.Destroy()
            self.note_list.ExpandAll()
        
    
    def on_close(self, event):
        # ask user save or not
        # if save, use funcion save()

        self.write_data_to_file()
        if self.Title[0] == '*':
            dialog = wx.MessageDialog(
                self, '是否保存笔记', '提示', wx.YES_NO | wx.ICON_INFORMATION)
            if dialog.ShowModal() == wx.ID_YES:
                self.save(None)
            dialog.Destroy()
        self.Destroy()
    def _get_theme_in_file(self, file_path=get_file('\\data\\theme\\default.theme.json')):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(data)
                self.theme = data
                return True
        except:
            return False

    def _write_theme_to_file(self, file_path=get_file('\\data\\theme\\default.theme.json')):
        try:
            with open(file_path, 'w') as f:
                f.write(str(self.theme))
                return True
        except:
            return False

    def set_theme(self, file_path):
        # set theme
        get = self._get_theme_in_file(file_path)
        if get == False:
            #notice user
            dialog = wx.MessageDialog(
                self, '主题文件导入失败', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return False
        try:
            #刷新界面
            self.m_panel26.SetBackgroundColour(
            wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            self.m_panel10.SetBackgroundColour(
            (wx.Colour(eval(self.theme["notebook_left"]["colour"]))))


            self.m_staticText9.SetFont(
            wx.Font(
                24, eval(self.theme["default_font"]["family"]),
                eval(self.theme["default_font"]["style"]),
                eval(self.theme["default_font"]["weight"]), False if
                self.theme["default_font"]["underline"] == "false" else True,
                self.theme["default_font"]["face_name"]))
            self.m_staticText9.SetForegroundColour(
            wx.Colour(eval(self.theme["default_font"]["colour"])))
            self.note_list.SetForegroundColour(wx.Colour(eval(self.theme["default_font"]["colour"])))
            self.note_list.SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_left"]["colour"])))
            self.note_list.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.morning_night.SetFont(
            wx.Font(self.theme["morning_night_topic"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]), eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.morning_night.SetForegroundColour(wx.Colour(eval(self.theme["morning_night_topic"]["colour"])))
            self.time_text.SetFont(
            wx.Font(self.theme["time_text"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]), eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.time_text.SetForegroundColour(wx.Colour(eval(self.theme["time_text"]["colour"])))
            self.m_button1.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.m_button11.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.m_button111.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            
            self.on_enter_window(None)
            self.on_leave_window(None)
            
            

            self.Refresh()
            self.Update()
            self.Layout()
        except:
            #notice user
            dialog = wx.MessageDialog(
                self, '主题文件加载失败', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return False
        return True
    
    def edit_theme(self, event=None):
        app = SettingFrame(self)
        app.Show()
        app.open(1)

    def on_enter_window(self, event=None):
        try:
            #change button background color
            event.GetEventObject().SetBackgroundColour(
                wx.Colour(39, 44, 52))
            event.GetEventObject().SetForegroundColour(
                wx.Colour(255, 255, 255))
        except:
            self.m_button1.SetBackgroundColour(
                wx.Colour(39, 44, 52))
            self.m_button1.SetForegroundColour(
                wx.Colour(255, 255, 255))

            self.m_button11.SetBackgroundColour(
                wx.Colour(39, 44, 52))
            self.m_button11.SetForegroundColour(
                wx.Colour(255, 255, 255))

            self.m_button111.SetBackgroundColour(
                wx.Colour(39, 44, 52))
            self.m_button111.SetForegroundColour(
                wx.Colour(255, 255, 255))
        

    def on_leave_window(self, event=None):
        try:
            #change button background color
            event.GetEventObject().SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            event.GetEventObject().SetForegroundColour(wx.Colour(font_colour))
        except:
            self.m_button1.SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button1.SetForegroundColour(wx.Colour(font_colour))

            self.m_button11.SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button11.SetForegroundColour(wx.Colour(font_colour))

            self.m_button111.SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button111.SetForegroundColour(wx.Colour(font_colour))

    def __del__(self):
        pass

    




if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
