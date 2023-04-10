# standard
import datetime

# wx
import wx

# agpg
from agrecorder.agpg import AGPG
# agrp
from agrecorder.agrp import AGRP
# window
from agrecorder.window.window import Window


# ag record window
class AGRW(Window):

    # public

    ONE_WEEK = 7

    def __init__(self, agpg: AGPG, agrp: AGRP):
        super().__init__(None)
        self.agpg = agpg
        self.agrp = agrp

        # 1週間分のページを作成
        self.panel_pgs = []
        self.listctrl_pgs = []

        for i in range(self.ONE_WEEK):
            panel_pg = wx.Panel(self.notebook_pgdates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sizer_pg = wx.BoxSizer(wx.VERTICAL)

            listctrl_pg = wx.ListCtrl(panel_pg, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
            sizer_pg.Add(listctrl_pg, 1, wx.ALL | wx.EXPAND, 0)

            panel_pg.SetSizer(sizer_pg)
            panel_pg.Layout()
            sizer_pg.Fit(panel_pg)
            self.notebook_pgdates.AddPage(panel_pg, f'{i+1}', False)

            self.panel_pgs.append(panel_pg)
            self.listctrl_pgs.append(listctrl_pg)

    def click_button_settings(self, event):
        event.Skip()
        print('click_button_settings')

    def click_button_agpgget(self, event):
        for i in range(self.ONE_WEEK):
            date = datetime.date.today() + datetime.timedelta(days=i)
            self.agpg.save(self.agpg.get_by_day(date), f"{date.strftime(self.agpg.DATE_FORMAT)}.json") #todo configの保存先を指定するようにする

    def click_button_agpgreload(self, event):
        for i in range(self.ONE_WEEK):
            date = datetime.date.today() + datetime.timedelta(days=i)
            self.agpg.load(f"{date.strftime(self.agpg.DATE_FORMAT)}.json") #todo configの保存先を指定するようにする

    def click_button_immediatelyrecord(self, event):
        event.Skip()
        print('click_button_immediatelyrecord')

    def click_button_play(self, event):
        event.Skip()
        print('click_button_play')

    def click_button_exit(self, event):
        self.Close()

    def click_button_reservedelete(self, event):
        event.Skip()
        print('click_button_reservedelete')

    def click_button_recordedplay(self, event):
        event.Skip()
        print('click_button_recordedplay')

    def click_button_recordeddelete(self, event):
        event.Skip()
        print('click_button_recordeddelete')

    def click_button_recordedopen(self, event):
        event.Skip()
        print('click_button_recordedopen')

