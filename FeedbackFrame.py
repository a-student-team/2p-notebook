from numpy import size
import wx
from wx import html2
import time
from get_file import get_file
class FeedbackFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="反馈", size=(650, 450))
        self.SetBackgroundColour("#FFFFFF")
        self.SetIcon(wx.Icon(get_file("\\images\\icon.ico"), wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)
        self.SetMinSize(wx.Size(650, 450))
        self.SetMaxSize(wx.Size(650, 450))
        self.sizer = wx.GridBagSizer(5, 5)
        
        #名字输入框和反馈内容输入框, 一个按钮提交
        self.name_text = wx.StaticText(self, label="名字:(选填)")
        self.name_input = wx.TextCtrl(self, value="")
        self.content_text = wx.StaticText(self, label="反馈内容:")
        self.content_input = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(500, 300))
        self.submit_button = wx.Button(self, label="提交")
        self.submit_button.Bind(wx.EVT_BUTTON, self.on_submit)
        #添加到sizer中
        self.sizer.Add(self.name_text, pos=(0, 0), flag=wx.ALL, border=5)
        self.sizer.Add(self.name_input, pos=(0, 1), span=(1, 2), flag=wx.ALL, border=5)
        self.sizer.Add(self.content_text, pos=(1, 0), flag=wx.ALL, border=5)
        self.sizer.Add(self.content_input, pos=(1, 1), span=(1, 2), flag=wx.ALL|wx.EXPAND, border=5)
        self.sizer.Add(self.submit_button, pos=(2, 1), flag=wx.ALL, border=5)
        
        #设置sizer
        self.SetSizer(self.sizer)
        
    def on_submit(self, event):
        url = "http://dage.world"
        #获取输入的内容, 并转换成列表, 像['名字', '反馈内容', '时间]
        if self.content_input.GetValue() == "":
            #notice user
            wx.MessageBox("反馈内容不能为空", "提示", wx.OK | wx.ICON_INFORMATION)
            return None
        if self.name_input.GetValue() == "":
            self.name_input.SetValue("匿名")
        name = self.name_input.GetValue()
        content = self.content_input.GetValue()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = [name, content, time_str]
        self.browser = html2.WebView.New(self)
        self.browser.LoadURL(url)
        #隐藏
        self.sizer.Add(self.browser, pos=(0, 3), span=(3, 1), flag=wx.ALL|wx.EXPAND, border=5)
        self.browser.Hide()
        #提交
        self.browser.RunScript("addCount({}, {})".format("notebook", data))
        
        
        
        
        #提示框
        wx.MessageBox("提交成功", "提示", wx.OK | wx.ICON_INFORMATION)
        
        self.Destroy()

#test
if __name__ == '__main__':
    app = wx.App()
    frame = FeedbackFrame(None)
    frame.Show()
    app.MainLoop()