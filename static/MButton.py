from tkinter import Button
from wx import Button
from wx import EVT_ENTER_WINDOW, EVT_LEAVE_WINDOW
import wx
class MButton(Button):
    def __init__(self, parent, text=" ", style=wx.NO_BORDER):
        Button.__init__(self, parent, wx.ID_ANY, text, style=style)
        self.enter_back = (39, 44, 52)
        self.enter_fore = (255, 255, 255)
        self.default_back = (247, 247, 247)
        self.default_fore = (8, 8, 8)
        self.Bind(EVT_ENTER_WINDOW, self.on_enter_window)
        self.Bind(EVT_LEAVE_WINDOW, self.on_leave_window)
        

        self.SetAutoLayout(True)

    def on_enter_window(self, event):
        self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        #change button background color
        self.SetBackgroundColour(
            wx.Colour(self.enter_back[0], self.enter_back[1], self.enter_back[2]))
        self.SetForegroundColour(
            wx.Colour(self.enter_fore[0], self.enter_fore[1], self.enter_fore[2]))
        self.Refresh()

    def on_leave_window(self, event):
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        #change button background color
        self.SetBackgroundColour(
            wx.Colour(self.default_back[0], self.default_back[1], self.default_back[2]))
        self.SetForegroundColour(
            wx.Colour(self.default_fore[0], self.default_fore[1], self.default_fore[2]))
        self.Refresh()

    def refresh(self):
        self.on_enter_window(None)
        self.on_leave_window(None)
        self.Refresh()

#test
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, "test")
    frame.SetSize(300, 300)
    frame.Show()
    button = MButton(frame, "test")
    button.SetSize(100, 100)
    button.refresh()
    app.MainLoop()

