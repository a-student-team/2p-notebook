
import wx
from wx.adv import CalendarCtrl, GenericCalendarCtrl
from get_file import get_file
from wx import adv
from static.MButton import MButton


class TimeFrame(wx.Frame):
    '''类似于日程表, 可以添加事件及其时间段, 到了相应的时间会提醒用户'''
    def __init__(self, parent, data=None):

        wx.Frame.__init__(self, parent, title='日程表', size=(450, 450))
        self.date_event = {} if data == None else data #日期:事件列表 , like {'2018-12-12':[{'event':'event1', 'time':'12:00', 'place':'place1', 'remark':'remark1'}, {'event':'event2', 'time':'12:00', 'place':'place2', 'remark':'remark2'}]}


        self.SetMinSize(wx.Size(450, 450))
        self.SetMaxSize(wx.Size(450, 450))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.init_ui()
        
        self.SetSizer(self.main_sizer)
        self.Center()
        self.Show()

        #设置图标
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(get_file("\\images\\icon.ico"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)


        self.refresh_today_event_list()



    def init_ui(self):
        #sizer中有一个日程表, 添加事件按键, 删除事件按键, 和今日日程表
        self.main_sizer = wx.GridBagSizer(5, 5)
        self.main_sizer.Add(self.init_calendar(), pos=(0, 0), span=(4, 1), flag=wx.ALL, border=0)
        
        self.main_sizer.Add(self.init_add_event_button(), pos=(0, 1), flag=wx.ALL, border=0)
        self.main_sizer.Add(self.init_delete_event_button(), pos=(1, 1), flag=wx.ALL, border=0)
        self.main_sizer.Add(self.init_to_today_event_button(), pos=(2, 1), flag=wx.ALL, border=0)
        self.main_sizer.Add(wx.StaticText(self, label='温馨提示: 需要关闭此窗口\n才有提示功能哦\n关闭时会自动保存日程表的'), pos=(3, 1), flag=wx.ALL, border=0)
        self.main_sizer.Add(self.init_today_event_list(), pos=(4, 0), span=(1, 2), flag=wx.EXPAND, border=0)
        
        
        self.main_sizer.AddGrowableCol(1)
        self.main_sizer.AddGrowableRow(2)

    def init_to_today_event_button(self):
        #初始化到今日事件按键
        self.to_today_event_button = MButton(self, '回到今天')
        self.to_today_event_button.Bind(wx.EVT_BUTTON, self.to_today_event)
        self.to_today_event_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.to_today_event_button

    def init_calendar(self):
        #初始化日历
        self.calendar = GenericCalendarCtrl(self, wx.ID_ANY, wx.DateTime.Today(), style=adv.CAL_SHOW_HOLIDAYS | adv.CAL_MONDAY_FIRST|adv.CAL_SHOW_SURROUNDING_WEEKS|adv.CAL_SEQUENTIAL_MONTH_SELECTION|wx.NO_BORDER)
        self.calendar.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        #当所选日期发生变化时, 就触发on_calendar_sel_changed事件
        self.calendar.Bind(adv.EVT_CALENDAR_SEL_CHANGED, self.on_calendar_sel_changed)
        self.calendar.Bind(wx.EVT_SIZE, self.on_calendar_size)
        return self.calendar
    def init_add_event_button(self):
        #初始化添加事件按键
        self.add_event_button = MButton(self, '添加事件')
        self.add_event_button.Bind(wx.EVT_BUTTON, self.add_event)
        self.add_event_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.add_event_button
    def init_delete_event_button(self):
        #初始化删除事件按键
        self.delete_event_button = MButton(self, '删除事件')
        self.delete_event_button.Bind(wx.EVT_BUTTON, self.delete_event)
        self.delete_event_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.delete_event_button
    def init_today_event_list(self):
        #初始化今日事件列表
        self.today_event_list = wx.ListCtrl(self, style=wx.LC_REPORT |wx.NO_BORDER)
        self.today_event_list.InsertColumn(0, '事件')
        self.today_event_list.InsertColumn(1, '时间')
        self.today_event_list.InsertColumn(2, '地点')
        self.today_event_list.InsertColumn(3, '备注')
        #设置备注一栏的宽度
        self.today_event_list.SetColumnWidth(3, 150)
        
        self.today_event_list.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.today_event_list

    def to_today_event(self, event):
        #回到今日事件
        self.calendar.SetDate(wx.DateTime.Today())
        self.refresh_today_event_list() 

    def refresh_today_event_list(self):
        print("refresh")
        #刷新今日事件列表
        self.today_event_list.DeleteAllItems()
        date = self.calendar.GetDate()
        date_str = date.FormatISODate()
        print(self.date_event)
        print(date_str)
        if date_str not in self.date_event:
            return

        for event in self.date_event[date_str]:
            #如果事件的时间(包含了日期和具体时间)是self.calendar.GetDate()的话, 就添加到今日事件列表
            if event["time"].startswith(date_str):
                self.today_event_list.InsertStringItem(0, event["event"])
                self.today_event_list.SetStringItem(0, 1, str(event["time"]))
                self.today_event_list.SetStringItem(0, 2, event["place"])
                self.today_event_list.SetStringItem(0, 3, event["remark"])
                self.today_event_list.SetItemData(0, 0)
        self.today_event_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.today_event_list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.today_event_list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.today_event_list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
    def on_calendar_size(self, event):
        #日历大小改变时, 更新日历
        self.calendar.SetSize(event.GetSize())
        self.calendar.Refresh()
        event.Skip()

    def add_event(self, event_):
        #添加事件
        self.add_event_dialog = AddEventDialog(self)
        self.add_event_dialog.ShowModal()
        self.add_event_dialog.Destroy()
        if not self.add_event_dialog.is_ok:
            return
        event = self.add_event_dialog.event_text.GetValue()
        #有两个time控件, 一个是选取时间, 一个是选取日期, 但是选取的日期包含时间00:00:00, 所以这里要把时间拆开
        time = self.add_event_dialog.time_choose.GetValue()
        date = self.add_event_dialog.date_choose.GetValue()
        
        time_str = date.FormatISODate() + ' ' + time.FormatISOTime()
        print(time_str)
    
        place = self.add_event_dialog.place_text.GetValue()
        remark = self.add_event_dialog.remark_text.GetValue()
        
        self.add_event_to_date(event, time_str, place, remark)

    def add_event_to_date(self, event, time, place, remark):
        #添加事件到日期
        date = time.split(' ')[0]
        
        if date in self.date_event:
            self.date_event[date].append(dict(event=event, time=time, place=place, remark=remark))
        else:
            self.date_event[date] = [dict(event=event, time=time, place=place, remark=remark)]
        self.refresh_today_event_list()

    def delete_event(self, event):
        #删除事件
        date = self.calendar.GetDate()
        #获取self.today_event_list中选中的事件
        index = self.today_event_list.GetFirstSelected()
        if index == -1:
            return
        event_str = self.today_event_list.GetItemText(index)
        #获取选中的事件的时间
        time_str = self.today_event_list.GetItem(index, 1).GetText()
        #在self.date_event中找到对应的事件并删除
        for event in self.date_event[date.FormatISODate()]:
            if event["event"] == event_str and event["time"] == time_str:
                self.date_event[date.FormatISODate()].remove(event)
                break
        self.refresh_today_event_list()

    def on_calendar_sel_changed(self, event):
        self.refresh_today_event_list()

class AddEventDialog(wx.Dialog):
    '''一个让用户输入其事件, 时间, 地点(可选), 备注(可选)的dialog'''
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title='添加事件', size=(400, 250))
        self.parent = parent
        self.is_ok = False
        self.SetMinSize(wx.Size(250, 250))

        self.init_ui()
        self.Center()
        self.Show()

    def init_ui(self):
        #初始化界面
        self.main_sizer = wx.GridBagSizer(5, 5)
        self.main_sizer.Add(self.init_event_label(), pos=(0, 0), flag=wx.ALL, border=5)
        self.main_sizer.Add(self.init_event_text(), pos=(0, 1), span=(1, 2), flag=wx.EXPAND, border=5)
        self.main_sizer.Add(self.init_time_label(), pos=(1, 0), flag=wx.ALL, border=5)
        self.main_sizer.Add(self.init_time_choose(), pos=(1, 1), span=(1, 2), flag=wx.EXPAND, border=5)
        self.main_sizer.Add(self.init_place_label(), pos=(2, 0), flag=wx.ALL, border=5)
        self.main_sizer.Add(self.init_place_text(), pos=(2, 1), span=(1, 2), flag=wx.EXPAND, border=5)
        self.main_sizer.Add(self.init_remark_label(), pos=(3, 0), flag=wx.ALL, border=5)
        self.main_sizer.Add(self.init_remark_text(), pos=(3, 1), span=(1, 2), flag=wx.EXPAND, border=5)
        self.main_sizer.Add(self.init_ok_button(), pos=(4, 0), flag=wx.ALL, border=5)
        self.main_sizer.Add(self.init_cancel_button(), pos=(4, 1), flag=wx.ALL, border=5)
        self.SetSizer(self.main_sizer)

    def init_event_label(self):
        #初始化事件标签
        self.event_label = wx.StaticText(self, label='事件')
        self.event_label.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.event_label

    def init_event_text(self):
        #初始化事件文本框
        self.event_text = wx.TextCtrl(self)
        self.event_text.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.event_text

    def init_time_label(self):
        #初始化时间标签
        self.time_label = wx.StaticText(self, label='时间')
        self.time_label.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.time_label

    def init_time_choose(self):
        #time choice, both choose the time and the date
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.date_choose = adv.DatePickerCtrl(self, size=(100, -1), style=adv.DP_DROPDOWN | adv.DP_SHOWCENTURY)
        self.time_choose = adv.TimePickerCtrl(self, size=(100, -1))
        self.date_choose.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        self.time_choose.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        self.sizer.Add(self.date_choose, 0, wx.ALL, 5)
        self.sizer.Add(self.time_choose, 0, wx.ALL, 5)
        
        return self.sizer

    def init_place_label(self):
        #初始化地点标签
        self.place_label = wx.StaticText(self, label='地点(可选)')
        self.place_label.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.place_label

    def init_place_text(self):
        #初始化地点文本框
        self.place_text = wx.TextCtrl(self)
        self.place_text.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.place_text

    def init_remark_label(self):
        #初始化备注标签
        self.remark_label = wx.StaticText(self, label='备注(可选)')
        self.remark_label.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.remark_label

    def init_remark_text(self):
        #初始化备注文本框
        #多行文本框
        self.remark_text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.remark_text.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        return self.remark_text

    def init_ok_button(self):
        #初始化确定按钮
        self.ok_button = MButton(self, '确定')
        self.ok_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok_button)
        return self.ok_button

    def init_cancel_button(self):
        #初始化取消按钮
        self.cancel_button = MButton(self, '取消')
        self.cancel_button.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '微软雅黑'))
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel_button)
        return self.cancel_button

    def on_ok_button(self, event):
        #确定按钮事件
        event_name = self.event_text.GetValue()
        event_date = self.date_choose.GetValue()
        print(event_date.FormatISODate())
        if not event_name:
            wx.MessageBox('事件不能为空!', '错误', wx.OK | wx.ICON_ERROR)
            return
        
        if event_date.FormatISODate() in self.parent.date_event:
            
            for i in self.parent.date_event[event_date.FormatISODate()]:
                if event_name == i["event"]:
                    wx.MessageBox('事件已存在!', '错误', wx.OK | wx.ICON_ERROR)
                    return
        self.is_ok = True
        self.Destroy()

    def on_cancel_button(self, event):
        #取消按钮事件
        self.Destroy()




if __name__ == '__main__':
    app = wx.App()
    TimeFrame(None)
    app.MainLoop()

