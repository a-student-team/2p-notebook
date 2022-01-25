import wx
from get_file import get_file
class NoBorderFrame(wx.Frame):
    # a frame that has a sizer without borders
    def __init__(self,
                 parent,
                 style=wx.DEFAULT_FRAME_STYLE,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 name=wx.FrameNameStr,):
        wx.Frame.__init__(self,
                          parent,
                          id=id,
                          title=title,
                          size=size,
                          pos=pos,
                          style=wx.NO_BORDER | style,
                          name=name)

        self.Center()
        self.Show(True)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        # a sizer like windows title bar
        self.sizer = wx.GridSizer(0, 0, 0, 0)

        # close button
        self.close_bitmap = wx.Bitmap(get_file('\\images\\close.png'),
                                      wx.BITMAP_TYPE_PNG)

        self.close_button = wx.BitmapButton(
            self,
            wx.ID_ANY,
            self.close_bitmap,
            style=wx.BU_AUTODRAW | wx.BORDER_NONE | wx.BU_RIGHT,
            size=(30, 30))
        # set background color like frame
        self.close_button.SetBackgroundColour(self.GetBackgroundColour())
        self.close_button.Bind(wx.EVT_ENTER_WINDOW, self.close_btn_enter_window)
        self.close_button.Bind(wx.EVT_LEAVE_WINDOW, self.close_btn_leave_window)

        self.sizer.Add(self.close_button, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.print_title_sizer()
        self.Layout()
        self.main_sizer.Add(self.sizer, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.print_screen()
        self.SetSizer(self.main_sizer)

        self.Layout()

        # bind events
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)
    
    def close_btn_enter_window(self, event):
        self.close_button.SetBackgroundColour(wx.Colour(245, 90, 83))
        self.close_button.Refresh()
        event.Skip()
    
    def close_btn_leave_window(self, event):
        self.close_button.SetBackgroundColour(self.GetBackgroundColour())
        self.close_button.Refresh()
        event.Skip()

    def print_title_sizer(self):
        pass

    def print_screen(self):
        pass

    def OnClose(self, event):
        self.Destroy()

    def OnMouse(self, event):

        if event.LeftDown():
            self.CaptureMouse()
            self.pos = event.GetPosition()
        elif event.LeftUp():
            self.ReleaseMouse()
        elif event.Dragging():
            if self.HasCapture():
                self.Move(self.GetPosition() + event.GetPosition())
                self.pos = event.GetPosition()
        event.Skip()
