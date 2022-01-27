import hashlib
import wx


from get_file import get_file
from EditFrame import EditFrame
from CreateDialog import CreateDialog
from FastNote import FastNote
from SettingDialog import SettingDialog
from encryption import encrypt, decrypt
from EncryptDialog import EncryptDialog
from HelpFrame import HelpFrame
from SelectFrame import SelectImportDialog, SelectExportDialog
from AboutFrame import AboutFrame
from NearlyFileDialog import NearlyFileDialog
from TimeFrame import TimeFrame
import os
import time
import json
from ui import MyFrame1


class MainFrame(MyFrame1):
    def __init__(self, parent):
        super().__init__(parent)
        self.root = self.note_list.AddRoot("所有笔记")
        self.books = {}  # dict of book name
        self.note_list.ExpandAll()  
        self.file_path = [] # list of file_path, like{"path1", "path2", ...}
        self.nearlyfileMenuItem = [self.file1, self.file2, self.file3, self.file4, self.file5]
        self.nearlyfileButton = [self.nearly_open_button, self.nearly_open_button2, self.nearly_open_button3, self.nearly_open_button4]
        self._note_list_is_changed = False
        # the data like {'book':{'type':'1','note':'content',...},...}
        self.note_data = {}
        self.date_event = {} #存储日程表的信息, like {'date':[{'event':'event1','time':'time1...}..],...}
        

        self.temp_text = "" #temp text for edit_browser
        
        #import data
        if self.get_note_data_in_file() == False:
            #create a new main.note file
            self.write_note_data_to_file()
        if self.get_data_in_file() == False:
            #create a new main.data file
            print("create a new main.data file")
            self.write_data_to_file()

        self._update_nearlyfile()
        self.refresh_note_list_from_note_data()

    def refresh_note_list_from_note_data(self):
        self.note_list.DeleteAllItems()
        self.note_list.AddRoot("所有笔记")
        for book in self.note_data:
            print(book)
            if self.note_data[book]['type'] == 1:
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book, image=0) #添加加密图标 
                
            else:
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
            for t, note in self.note_data[book].items():
                print(t, note)
                if t == "type" or t == "key":
                    continue
                self.note_list.AppendItem(book_item, t)
        self.note_list.ExpandAll()
    def _note_in_note_data(self, note, root=None):
        # check if note in note_data
        if not root:
            for book in self.note_data:
                if note in self.note_data[book]:
                    return True
        else:
            return note in self.note_data[root]
        return False
        
    def _book_in_note_data(self, book):
        # check if book in note_data
        if book in self.note_data:
            return True
        return False
        
    def _update_nearlyfile(self):
        # update nearlyfileMenu
        for i in range(5):
            try:
                self.nearlyfileMenuItem[i].SetItemLabel(self.file_path[i])
            except:
                self.nearlyfileMenuItem[i].SetItemLabel(" ")

        for i in range(4):
            try:
                self.nearlyfileButton[i].SetLabelText(self._get_simple_file_path(self.file_path[i], 35))
                self.nearlyfileButton[i].file_path = self.file_path[i]
                self.Show()
            except:
                self.nearlyfileButton[i].Hide()
        
        #如果 self.nearlyfileButton列表中的所有按钮都隐藏了，那么就提醒用户
        if self.nearlyfileButton[0].IsShown() == False and self.nearlyfileButton[1].IsShown() == False and self.nearlyfileButton[2].IsShown() == False and self.nearlyfileButton[3].IsShown() == False:
            self.nearly_open_text.SetLabel("oops, 没有最近打开的文件")
            self.nearly_open_button_more.Hide()
        else:
            self.nearly_open_text.SetLabel("你最近打开了...")
            self.nearly_open_button_more.Show()
        
        self.Layout()
        

    def write_data_to_file(self):
        #write data to file
        try:
            data = {"file_path": self.file_path, "date_event": self.date_event}
            with open(get_file('\\data\\main.data'), 'w', encoding="utf-8") as f:
                
                f.write(str(data))
                return True
        except:
            return False

    def get_data_in_file(self):
        #get data in file
        try:
            with open(get_file('\\data\\main.data'), 'r', encoding="utf-8") as f:
                data = eval(f.read())
                self.file_path = data['file_path']
                self.date_event = data['date_event']
                print(self.date_event)
                return True
        except:
            return False
            
    def get_select_data(self, data):
        # get select data
        try:
            self.note_data.update(data)
            
            print(self.note_data)
            return True
        except:
            return False

    def write_select_data(self, data, file_path):
        # write select data to file
        try:
            with open(file_path, 'w', encoding="utf-8") as f:
                f.write(str(data))
                return True
        except:
            return False
    def write_more_data_to_file(self, file_path=get_file("\\data\\main.data"), data=None):
        #write data to file
        try:
            with open(file_path, 'w+', encoding="utf-8") as f:
                if data:
                    f.write(str(data))
                else:
                    f.write(str(self.file_path))
                return True
        except:
            return False
    def get_more_data_in_file(self, file_path=get_file("\\data\\main.data")):
        #get data in file
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = eval(f.read())
                return data
        except:
            return None
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
                self, '发现有重名的文件, 将会合并(或删除), 是否继续导入?', '提示', wx.YES_NO| wx.ICON_INFORMATION)
                    
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
    
    def change_time(self, event):
        self.time_text.SetLabel(
            "时间:"+str(time.strftime('%Y-%m-%d %H:%M:%S')))

        mytime = time.localtime()
        self.morning_night.SetLabel("晚上好" if 18 < mytime.tm_hour < 23 else (
            "上午好" if 0 < mytime.tm_hour < 12 else "下午好"))
        
    def edit_browser_open(self, event, root=None):
        pass
        
    def edit_frame_close(self, event):
        self.edit_browser_save()
        self.frame.Destroy()
        self.note_list_is_changed()
    def edit_browser_save(self, event=None, root=None, object=None):
        #ask user save or not
        # if save, use html2.runScript the function getText() to get text and save it into note_data
        if root == None:
            root = self.note_list.GetSelection()
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            return None
        else:
            
            text = self.frame.browser.RunScript("getText()")
            #将text中的所有/r/n替换成\n
            text = text[1].replace("\r\n", "\\n")
            if self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))]["type"] != 1:
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)] = text
            else:
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)] = encrypt(text, self._key)
            print(self.note_data)
            self.note_list.ExpandAll()
        
    
    def on_close(self, event):
        # ask user save or not
        # if save, use funcion save()

        self.write_data_to_file()

        if self._note_list_is_changed:
            dialog = wx.MessageDialog(
                self, '是否保存笔记', '提示', wx.YES_NO | wx.ICON_INFORMATION)
            if dialog.ShowModal() == wx.ID_YES:
                self.save(None)
            dialog.Destroy()
        
        try:
            self.fastnote.Destroy()
            self.frame.Destroy()
        except:
            pass
        self.Destroy()

    def sort_note_list(self):
        # sort note list
        self.note_list.SortChildren(self.note_list.GetRootItem())

    def note_list_is_changed(self, event=None):
        
        self._note_list_is_changed = True
        #set win topic a "*"
        print(self.Title)
        self.Title = "*" + self.Title if self.Title[0] != "*" else self.Title

    
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
        try:
            name = str(CreateDialog(self, "新笔记").m_textCtrl1.GetValue())
        except:
            return None

        if name == '':
            return None

        if self._note_in_note_data(name, self.note_list.GetItemText(root)):
            dialog = wx.MessageDialog(
                self, '名字重复啦, 笔记已存在', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None
        #print(self.note_data[self.note_list.GetItemText(root)])

        item = self.note_list.AppendItem(root, name)
        self.note_list.SelectItem(item)

        self.note_list.Expand(root)
        self.note_list.ExpandAll()
        
        self.note_list_is_changed()

        self.sort_note_list()

        
        self.note_data[self.note_list.GetItemText(root)][name] = ''


    def new_book(self, event):
        #add new book

        dialog = CreateDialog(self, "新笔记本", True)
        try:
            name = str(dialog.m_textCtrl1.GetValue())
        except:
            return None
        if self._book_in_note_data(name):
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

            self.note_list.AppendItem(self.note_list.GetRootItem(), name, image=0)
            book = self.note_list.FindItem(self.note_list.GetRootItem(), name)
            
            #添加本地图标icon.ico
            
            self.note_list.Expand(self.note_list.GetRootItem())
            self.note_list.ExpandAll()

            
            self.note_data[name] = {"type":1, "key":hashlib.md5(key.encode()).hexdigest()}
            
        else:

            self.note_list.AppendItem(self.note_list.GetRootItem(), name)
            book = self.note_list.FindItem(self.note_list.GetRootItem(), name)
            
            self.note_list.Expand(self.note_list.GetRootItem())
            self.note_list.ExpandAll()
            self.books[name] = book
            self.note_data[name] = {"type":0}
        self.note_list.SelectItem(book)
            
        print(self.books, self.note_list)
        self.sort_note_list()

        self.note_list_is_changed()
        

        
    
    def open_menu_file(self, file_path):
        if file_path == "":
            return False
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
        self._update_nearlyfile()
        self.note_list.DeleteAllItems()
        self.note_list.AddRoot("所有笔记")
        for book in self.note_data:
            book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
            for note in self.note_data[book]:
                self.note_list.AppendItem(book_item, note)
        self.note_list.ExpandAll()
    def about(self, event=None):
        frame = AboutFrame(self)
        frame.Show()

    def select_open(self, event=None):
        frame = SelectImportDialog(self)
        frame.ShowModal()

        get = frame.check_tree
        file_path = frame.file_path

        print(get)
        if get != []:
            self.file_path.append(file_path)
            if not self.get_select_data(get):
                message = wx.MessageDialog(self, '导入失败', '提示', wx.OK | wx.ICON_INFORMATION)   
                message.ShowModal()
                message.Destroy()
            else:
               
                if file_path not in self.file_path:
                    self.file_path.append(file_path)
                self._update_nearlyfile()
                self.note_list.DeleteAllItems()
                self.note_list.AddRoot("所有笔记")
                for book in self.note_data:
                    book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
                    for note in self.note_data[book]:
                        self.note_list.AppendItem(book_item, note)
                self.note_list.ExpandAll()
                message = wx.MessageDialog(self, '导入成功', '提示', wx.OK | wx.ICON_INFORMATION)
                message.ShowModal()
                message.Destroy()
        else:
            return None

    def select_save(self, event=None):
        frame = SelectExportDialog(self, self.note_data)
        frame.ShowModal()

        get = frame.check_tree
        file_path = frame.file_path     

        print(get)
        if get != []:
            self.file_path.append(file_path)
            if not self.write_select_data(get, file_path):
                message = wx.MessageDialog(self, '导出失败', '提示', wx.OK | wx.ICON_INFORMATION)   
                message.ShowModal()
                message.Destroy()
            else:
                message = wx.MessageDialog(self, '导出成功', '提示', wx.OK | wx.ICON_INFORMATION)
                message.ShowModal()
                message.Destroy()
        else:
            return None
    
    def open_note(self, event):
        # use EditFrame
        # if item's parent is root , don't open it
        
        
        '''if self.temp_text != self.frame.browser.RunScript("getText()")[1] and self.edit_panel.IsShown():
            
            dialog = wx.MessageDialog(
                self, '笔记未保存，是否保存？', '提示', wx.YES_NO | wx.ICON_INFORMATION)
            if dialog.ShowModal() == wx.ID_YES:
                self.save(None)
            dialog.Destroy()'''
        root = self.note_list.GetSelection()
        self.selectioned = root
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            return None
        if root == self.note_list.GetRootItem():
            return None
        
        '''self.edit_panel.SetSize(self.GetSize()[0]-self.m_panel10.GetSize()[0], self.m_panel10.GetSize()[1])
        self.edit_panel.browser.SetSize(self.edit_panel.GetSize()[0], self.edit_panel.GetSize()[1])
        '''         
        
        if self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))]["type"] == 1:
            text = self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)]
            #如果加密, 则提醒用户输入密码解密
        
            dialog = EncryptDialog(self, '')
            dialog.ShowModal()
            self._key = str(dialog.m_textCtrl1.GetValue())
            if hashlib.md5(self._key.encode('utf-8')).hexdigest() != self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))]["key"]:
                message = wx.MessageDialog(self, '密码错误', '提示', wx.OK | wx.ICON_INFORMATION)   
                message.ShowModal()
                message.Destroy()
                return None
            print(text)
            if text != "":
                text = decrypt(text, self._key)
            else:
                text = ""
        else:
            text = self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][self.note_list.GetItemText(root)]
        #创建临时text用于判断是否改变文本
        self.temp_text = text
        
        ''' self.edit_panel.browser.LoadURL(get_file('\\html\\edit.html?text={}'.format(text)))
        self.edit_panel.Show()
        self.gbSizer2_panel.Hide()
        # when it open, give a value to edit_browser.browser
        self.edit_panel.Bind(html2.EVT_WEBVIEW_LOADED, lambda event: self.edit_browser_open(event, root))'''
        self.frame = EditFrame(self, title="编辑笔记", size=(800, 600))
        self.frame.browser.LoadURL(get_file('\\html\\edit.html?text={}'.format(text)))
        self.frame.Show()
        self.frame.Bind(wx.EVT_CLOSE, self.edit_frame_close)
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
            self.gbSizer2_panel.SetBackgroundColour(
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
            self.welcome.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]), wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.welcome.SetForegroundColour(wx.Colour(eval(self.theme["morning_night_topic"]["colour"])))
            self.help_text.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]), wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.help_text.SetForegroundColour(wx.Colour(eval(self.theme["morning_night_topic"]["colour"])))
            self.nearly_open_text.SetFont(
            wx.Font(self.theme["default_font"]["size"]+3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]), wx.FONTWEIGHT_BOLD, False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_text.SetForegroundColour(wx.Colour(eval(self.theme["morning_night_topic"]["colour"])))
            self.m_button1.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.m_button11.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.m_button111.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.help_button.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_button.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_button2.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_button3.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_button4.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.nearly_open_button_more.SetFont(
            wx.Font(self.theme["default_font"]["size"]-3, eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            self.calendar_button.SetFont(
                wx.Font(self.theme["default_font"]["size"], eval(self.theme["default_font"]["family"]), eval(self.theme["default_font"]["style"]),eval(self.theme["default_font"]["weight"]), False if self.theme["default_font"]["underline"] == "false" else True, self.theme["default_font"]["face_name"]))
            
            
            self.m_button1.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button1.default_fore = (font_colour)

            self.m_button11.default_back = wx.Colour(eval(self.theme["notebook_right"]["colour"]))
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button11.default_fore = (font_colour)

            self.m_button111.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.m_button111.default_fore = (font_colour)

            self.help_button.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.help_button.default_fore = (font_colour)

            self.nearly_open_button.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.nearly_open_button.default_fore = (font_colour)

            self.nearly_open_button2.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.nearly_open_button2.default_fore = (font_colour)

            self.nearly_open_button3.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.nearly_open_button3.default_fore = (font_colour)

            self.nearly_open_button4.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.nearly_open_button4.default_fore = (font_colour)

            self.calendar_button.default_back = eval(self.theme["notebook_right"]["colour"])
            font_colour = eval(self.theme["notebook_right"]["colour"])
            #颜色取反
            font_colour = (255 - font_colour[0], 255 - font_colour[1], 255 - font_colour[2])
            self.calendar_button.default_fore = (font_colour)



            self.nearly_open_button_more.default_back = eval(self.theme["notebook_right"]["colour"])
            self.nearly_open_button_more.enter_back = eval(self.theme["notebook_right"]["colour"])
            self.m_button1.refresh()
            self.m_button11.refresh()
            self.m_button111.refresh()
            self.help_button.refresh()
            self.nearly_open_button.refresh()
            self.nearly_open_button2.refresh()
            self.nearly_open_button3.refresh()
            self.nearly_open_button4.refresh()
            self.nearly_open_button_more.refresh()
            self.nearly_open_button_more.refresh()
            self.calendar_button.refresh()
            self.m_button1.SetBackgroundColour(eval(self.theme["notebook_right"]["colour"]))
            
            
            
            #try:
                #self.frame.browser.RunScript(
                    #"setBackgroundColor({}, {})".format(str(self.theme["notebook_left"]["colour"]), str(self.theme["notebook_right"]["colour"])))
            #except:
                #pass

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
        app = SettingDialog(self)
        app.Show()
        app.open(1)


    '''def on_key_down(self, event):
        key = event.GetKeyCode()
        print(key)
        #按下ctrl+s保存
        if event.ControlDown() and key == 83:
            self.save()
        #按下ctrl+o打开
        if event.ControlDown() and key == 79:
            self.open()
'''
    def open_nearly_data(self, event):
        #get the event object'text and open the paper
        file_path = event.GetEventObject().file_path
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
        
        self._update_nearlyfile()
        self.note_list.DeleteAllItems()
        self.note_list.AddRoot("所有笔记")
        for book in self.note_data:
            book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
            for note in self.note_data[book]:
                self.note_list.AppendItem(book_item, note)
        self.note_list.ExpandAll()
        self.Layout()

    def _get_simple_file_path(self, file_path:str, len_string=20):
        file_name = file_path.split("\\")[-1]
        print(file_name)
        len_file_path = len_string - len(file_name) - 3
        print(len_file_path)
        return file_path[0:len_file_path] + "..." + file_name

    def address_on_enter_window(self, event):
        if event:
            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            event.GetEventObject().SetForegroundColour(
                wx.Colour(46, 177, 240))
            '''event.GetEventObject().SetFont(
            wx.Font(event.GetEventObject().GetFont().SetUnderlined(True))
            )'''
        else:
            self.nearly_open_button_more.SetBackgroundColour(
                wx.Colour(118, 134, 148))
            self.nearly_open_button_more.SetForegroundColour(
                wx.Colour(46, 177, 240))

    def address_on_leave_window(self, event):
        if event:
            self.SetCursor(wx.Cursor(wx.CURSOR_DEFAULT))
            event.GetEventObject().SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            event.GetEventObject().SetForegroundColour(wx.Colour(98, 148, 193))
        else:
            self.nearly_open_button_more.SetBackgroundColour(
                wx.Colour(eval(self.theme["notebook_right"]["colour"])))
            self.nearly_open_button_more.SetForegroundColour(wx.Colour(98, 148, 193))
        
    def open_nearly_data_more(self, event):
        dialog = NearlyFileDialog(self, self.file_path)
        dialog.ShowModal()
        import_file_path_lst = dialog.check_file_path
        print(import_file_path_lst)
        if import_file_path_lst:
            for file_path in import_file_path_lst:
                self.get_note_data_in_file(file_path)
                self.note_list.DeleteAllItems()
                self.note_list.AddRoot("所有笔记")
                for book in self.note_data:
                    book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
                    for note in self.note_data[book]:
                        self.note_list.AppendItem(book_item, note)
                self.note_list.ExpandAll()
            
    
    def __del__(self):
        pass

    def new_note(self, event):
        self.fastnote = FastNote(self)
        self.fastnote.Show()

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
        print(id)
        
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
            self.open_menu_file(self.file1.GetItemLabelText())
        elif id == wx.ID_FILE2:
            self.open_menu_file(self.file2.GetItemLabelText())
        elif id == wx.ID_FILE3:
            self.open_menu_file(self.file3.GetItemLabelText())
        elif id == wx.ID_FILE4:
            self.open_menu_file(self.file4.GetItemLabelText())
        elif id == wx.ID_FILE5:
            self.open_menu_file(self.file5.GetItemLabelText())
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
        elif id == self.ID_SETTING:
            self.setting()
        elif id == self.ID_SELECT_OPEN:
            self.select_open()
        elif id == self.ID_SELECT_SAVE:
            self.select_save()
        elif id == wx.ID_ABOUT:
            self.about()
        else:
            event.Skip()
    def help(self, event=None):
        frame = HelpFrame(self)
        frame.Show()

    def setting(self, event=None):
        frame = SettingDialog(self)
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
        self._update_nearlyfile()
        self._note_list_is_changed = False
        
            
        dialog.Destroy()
    def save(self, event=None):
        
        self.write_note_data_to_file()
        self._note_list_is_changed = False
        self.Title = self.Title[1:] if self.Title[0] == "*" else self.Title
        

    def open(self, event=None):
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
            self._update_nearlyfile()
            self.note_list.DeleteAllItems()
            self.note_list.AddRoot("所有笔记")
            for book in self.note_data:
                book_item = self.note_list.AppendItem(self.note_list.GetRootItem(), book)
                for note in self.note_data[book]:
                    self.note_list.AppendItem(book_item, note)
            self.note_list.ExpandAll()
            print(self.file_path)
            #self.note_list.Expand(self.root)
            
        dlg.Destroy()


    def rename_paper(self, event):
        root = self.note_list.GetSelection()
        name = CreateDialog(self).m_textCtrl1.GetValue()
        #如果root所在的note_data的笔记本有"key"键, 则提醒用户解密
        if name == '':
            return None
        if root == self.note_list.GetRootItem():
            dialog = wx.MessageDialog(
                self, '笔记区开头不能重命名', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            return None
        if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
            if self.note_data[self.note_list.GetItemText(root)].get("key") != None:
                    dialog = EncryptDialog(self, '')
                    dialog.ShowModal()
                    key = str(dialog.m_textCtrl1.GetValue())
                    if hashlib.md5(key.encode('utf-8')).hexdigest() != self.note_data[self.note_list.GetItemText(root)]["key"]:
                        message = wx.MessageDialog(self, '密码错误', '提示', wx.OK | wx.ICON_INFORMATION)   
                        message.ShowModal()
                        message.Destroy()
                        return None
            self.note_data[name] = self.note_data.pop(self.note_list.GetItemText(root))
        else:
            if self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].get("key") != None:
                    dialog = EncryptDialog(self, '')
                    dialog.ShowModal()
                    key = str(dialog.m_textCtrl1.GetValue())
                    if hashlib.md5(key.encode('utf-8')).hexdigest() != self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))]["key"]:
                        message = wx.MessageDialog(self, '密码错误', '提示', wx.OK | wx.ICON_INFORMATION)   
                        message.ShowModal()
                        message.Destroy()
                        return None
            self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))][name] = self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))
        
        self.note_list.SetItemText(root, name)
        
        self.note_list_is_changed()

    def delete_paper(self, event):
        root = self.note_list.GetSelection()
        #如果root所在的note_data的笔记本有"key"键, 则提醒用户解密
        if root != self.note_list.GetRootItem():
            if self.note_list.GetItemParent(root) == self.note_list.GetRootItem():
                if self.note_data[self.note_list.GetItemText(root)].get("key") != None:
                    dialog = EncryptDialog(self, '')
                    dialog.ShowModal()
                    key = str(dialog.m_textCtrl1.GetValue())
                    if hashlib.md5(key.encode('utf-8')).hexdigest() != self.note_data[self.note_list.GetItemText(root)]["key"]:
                        message = wx.MessageDialog(self, '密码错误', '提示', wx.OK | wx.ICON_INFORMATION)   
                        message.ShowModal()
                        message.Destroy()
                        return None
                self.note_data.pop(self.note_list.GetItemText(root))
            else:
                if self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].get("key") != None:
                    dialog = EncryptDialog(self, '')
                    dialog.ShowModal()
                    key = str(dialog.m_textCtrl1.GetValue())
                    if hashlib.md5(key.encode('utf-8')).hexdigest() != self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))]["key"]:
                        message = wx.MessageDialog(self, '密码错误', '提示', wx.OK | wx.ICON_INFORMATION)   
                        message.ShowModal()
                        message.Destroy()
                        return None
                self.note_data[self.note_list.GetItemText(self.note_list.GetItemParent(root))].pop(self.note_list.GetItemText(root))
        else:
            dialog = wx.MessageDialog(
                self, '删除失败', '提示', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()
            dialog.Destroy()
            
            return None

        
        self.note_list.Delete(root)
        
        self.gbSizer2_panel.Show()
        
        self.note_list_is_changed()
    def on_search(self, event):
        #get the search text, and search the note_data, and show the result in the note_list
        #if the search text is empty, show all the note_data
        search_text = self.m_searchCtrl1.GetValue()
        if search_text == '':
            self.refresh_note_list_from_note_data()
            self.m_searchCtrl1.ShowCancelButton(False)
            return None
        self.m_searchCtrl1.ShowCancelButton(True)
        self.note_list.DeleteAllItems()
        self.note_list.AddRoot('搜索结果')
        #the note_data is a dict but like tree, it has two levels, use the best way to search
        for key in self.note_data:
            if key.find(search_text) != -1:
                self.note_list.AppendItem(self.note_list.GetRootItem(), key)
            for key2 in self.note_data[key]:
                if key2.find(search_text) != -1:
                    self.note_list.AppendItem(self.note_list.GetLastChild(self.note_list.GetRootItem()), key2)
        
        self.note_list.Expand(self.note_list.GetRootItem())
        self.note_list.ExpandAll()

    def on_search_cancel(self, event):
        self.m_searchCtrl1.SetValue('')
        if self.note_list.GetItemText(self.note_list.GetRootItem()) == "搜索结果":
            self.refresh_note_list_from_note_data()

    def on_calendar_button(self, event):
        self.timeframe = TimeFrame(self, self.date_event)
        self.timeframe.Bind(wx.EVT_CLOSE, self._on_timeframe_close)


    def _on_timeframe_close(self, event):
        self.date_event = self.timeframe.date_event
        self.timeframe.Destroy()

    def clock(self, event):
        #通过date_event获取今天的日期, 判断事件的时间是否已经到了, 如果到了, 则提醒用户
        tp = time.strftime('%Y-%m-%d', time.localtime())
        if tp not in self.date_event:
            return None
        #if time.strftime('%H:%M', time.localtime()) in self.date_event[tp]:
        tp1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        for event_range in range(len(self.date_event[tp])):
            if self.date_event[tp][event_range]["time"] == tp1:
                dialog = wx.MessageDialog(self, '事件[{}]的时间已经到了\n地点:{}\n备注:{}'.format(self.date_event[tp][event_range]["event"], self.date_event[tp][event_range]["place"] if self.date_event[tp][event_range]["place"] != "" else "无", self.date_event[tp][event_range]["remark"] if self.date_event[tp][event_range]["remark"] != "" else "无"), '提醒', wx.OK | wx.ICON_INFORMATION)
                dialog.ShowModal()
                dialog.Destroy()
                return None
        return None
                


    




if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()
