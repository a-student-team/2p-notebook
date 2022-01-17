import imp
import wx
import wx.lib.agw.customtreectrl as ct
class SelectImportDialog(wx.Dialog):
    def __init__(self, parent, ):
        super().__init__(parent, wx.ID_ANY, title="选择导入", size = (300, 700))
        # 创建面板
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.tree = ct.CustomTreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 600), agwStyle=wx.TR_DEFAULT_STYLE|ct.TR_AUTO_CHECK_CHILD|ct.TR_AUTO_CHECK_PARENT|wx.TR_HIDE_ROOT)
        root = self.tree.AddRoot("root", ct_type=1)
        sizer.Add(self.tree, 0, wx.ALL)
        #创建按钮
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_import = wx.Button(self, wx.ID_ANY, "导入")
        self.btn_cancel = wx.Button(self, wx.ID_ANY, "取消")
        btn_sizer.Add(self.btn_import, 1, wx.ALL, 5)
        btn_sizer.Add(self.btn_cancel, 1, wx.ALL, 5)
        sizer.Add(btn_sizer, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        

        self.check = []

        #选择文件
        file_dialog = wx.FileDialog(self, message="选择文件", style=wx.FD_OPEN, wildcard="*.note")
        if file_dialog.ShowModal() == wx.ID_OK:
            self.file_path = file_dialog.GetPath()
            if self.file_path == "":
                return None
        file_dialog.Destroy()
        #获取文件信息
        with open(self.file_path, 'r', encoding="utf-8") as f:
            self.file_info = eval(f.read())

        for book in self.file_info:
            if book.find("NgsAABwEVA==")!= -1:
                print(book)
                book_item = self.tree.AppendItem(self.tree.GetRootItem(), book[12:], ct_type=1) 
                
            else:
                print(book)
                book_item = self.tree.AppendItem(self.tree.GetRootItem(), book, ct_type=1)
            for t, note in self.file_info[book].items():
                print(t, note)
                if t == "type":
                    continue
                self.tree.AppendItem(book_item, t, ct_type=0)
        self.tree.ExpandAll()
        self.btn_import.Bind(wx.EVT_BUTTON, self.OnImport)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        self.tree.Bind(ct.EVT_TREE_ITEM_CHECKED, self.OnCheck)
        
    def OnCheck(self, event):
        self.check.append(event.GetItem())

    def OnImport(self, event):
        #将check列表依照tree变化成树
        self.check_tree = {}
        for item in self.check:
            try:
                self.check_tree[self.tree.GetItemText(item)] = self.file_info[self.tree.GetItemText(item)]
            except:
                self.check_tree["NgsAABwEVA==" + self.tree.GetItemText(item)] = self.file_info["NgsAABwEVA==" + self.tree.GetItemText(item)]
        self.Destroy()

    def OnCancel(self, event):
        self.Destroy()
class SelectExportDialog(wx.Dialog):
    def __init__(self, parent, data):
        super().__init__(parent, wx.ID_ANY, title="选择导出", size = (300, 700))
        # 创建面板
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.tree = ct.CustomTreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 600), agwStyle=wx.TR_DEFAULT_STYLE|ct.TR_AUTO_CHECK_CHILD|ct.TR_AUTO_CHECK_PARENT|wx.TR_HIDE_ROOT)
        root = self.tree.AddRoot("root", ct_type=1)
        sizer.Add(self.tree, 0, wx.ALL)
        #创建按钮
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_export = wx.Button(self, wx.ID_ANY, "导出")
        self.btn_cancel = wx.Button(self, wx.ID_ANY, "取消")
        btn_sizer.Add(self.btn_export, 1, wx.ALL, 5)
        btn_sizer.Add(self.btn_cancel, 1, wx.ALL, 5)
        sizer.Add(btn_sizer, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()
        self.Centre(wx.BOTH)
        

        self.check = []

        #选择导出的路径
        file_dialog = wx.FileDialog(self, message="选择文件", style=wx.FD_SAVE, wildcard="*.note")
        if file_dialog.ShowModal() == wx.ID_OK:
            self.file_path = file_dialog.GetPath()
            if self.file_path == "":
                return None
        file_dialog.Destroy()
        self.file_info = data

        for book in self.file_info:
            if book.find("NgsAABwEVA==")!= -1:
                print(book)
                book_item = self.tree.AppendItem(self.tree.GetRootItem(), book[12:], ct_type=1) 
                
            else:
                print(book)
                book_item = self.tree.AppendItem(self.tree.GetRootItem(), book, ct_type=1)
            for t, note in self.file_info[book].items():
                print(t, note)
                if t == "type":
                    continue
                self.tree.AppendItem(book_item, t, ct_type=0)
        self.tree.ExpandAll()
        self.btn_export.Bind(wx.EVT_BUTTON, self.OnExport)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        self.tree.Bind(ct.EVT_TREE_ITEM_CHECKED, self.OnCheck)

    def OnCheck(self, event):
        self.check.append(event.GetItem())

    def OnExport(self, event):
        #将check列表依照tree变化成树
        self.check_tree = {}
        for item in self.check:
            try:
                self.check_tree[self.tree.GetItemText(item)] = self.file_info[self.tree.GetItemText(item)]
            except:
                self.check_tree["NgsAABwEVA=="+self.tree.GetItemText(item)] = self.file_info["NgsAABwEVA=="+self.tree.GetItemText(item)]
        self.Destroy()

    def OnCancel(self, event):
        self.Destroy()
        
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = SelectImportDialog(None)
    frame.ShowModal()
    app.MainLoop()