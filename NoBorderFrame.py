import wx
from get_file import get_file
class NoBorderFrame(wx.Frame):
    # a frame that has a sizer without borders
    def __init__(self,
                 parent,
                 id=wx.ID_ANY,
                 title=wx.EmptyString,
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=wx.NO_BORDER,
                 name=wx.FrameNameStr):
        wx.Frame.__init__(self,
                          parent,
                          id=id,
                          title=title,
                          size=size,
                          pos=pos,
                          style=style,
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
            size=(self.close_bitmap.GetWidth() + 5,
                  self.close_bitmap.GetHeight() + 5))
        # set background color like frame
        self.close_button.SetBackgroundColour(self.GetBackgroundColour())
        self.close_button.SetBitmapFocus(
            wx.Bitmap(get_file('\\images\\close_focus.png'),
                      wx.BITMAP_TYPE_PNG))

        self.sizer.Add(self.close_button, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.Layout()
        self.main_sizer.Add(self.sizer, 0, wx.ALL | wx.ALIGN_RIGHT, 0)
        self.print_screen()
        self.SetSizer(self.main_sizer)

        self.Layout()

        # bind events
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

    def print_screen(self):
        pass

    def OnClose(self, event):
        self.Destroy()

    def OnMouse(self, event):
        # move like windows title bar
        if event.LeftDown():
            self.CaptureMouse()
            self.pos = event.GetPosition()

        elif event.LeftUp():
            self.ReleaseMouse()
        #move like windows title bar
        elif event.Dragging():
            if self.HasCapture():
                pos = event.GetPosition()

                self.Move(self.GetPosition() + event.GetPosition())
                self.pos = pos
        '''if event.LeftDown():
            self.CaptureMouse()
            self.pos = event.GetPosition()
        elif event.LeftUp():
            self.ReleaseMouse()
        elif event.Dragging():
            if self.HasCapture():
                self.Move(self.GetPosition() + event.GetPosition())
                self.pos = event.GetPosition()
        event.Skip()'''
