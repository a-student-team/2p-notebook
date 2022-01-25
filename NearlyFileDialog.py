import wx
import wx.lib.agw.customtreectrl as ct
class NearlyFileDialog(wx.Dialog):
    def __init__(self, parent, file_path:list):
        super().__init__(parent, size=wx.Size(300, 700), title="最近文件")
        # 创建面板
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.tree = ct.CustomTreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 600), agwStyle=wx.TR_DEFAULT_STYLE|ct.TR_AUTO_CHECK_CHILD|ct.TR_AUTO_CHECK_PARENT|ct.TR_NO_LINES)
        root = self.tree.AddRoot("全选", ct_type=1)
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
        for path in file_path:
            self.tree.AppendItem(self.tree.GetRootItem(), str(path), ct_type=1) 

        self.tree.ExpandAll()
        self.tree.Bind(ct.EVT_TREE_ITEM_CHECKED, self.OnCheck)
        self.btn_import.Bind(wx.EVT_BUTTON, self.OnImport)
        self.btn_cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
        
    def OnCheck(self, event):
        self.check.append(event.GetItem())
    def OnImport(self, event):
        self.check_file_path = [self.tree.GetItemText(i) for i in self.check]
        self.Destroy()
    def OnCancel(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    NearlyFileDialog(None, [i for i in range(1, 100)]).Show()
    app.MainLoop()
