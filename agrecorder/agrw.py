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
        self.app = wx.App()

        super().__init__(None)
        self.agpg = agpg
        self.agrp = agrp

        # 1週間分のページを作成
        self.panel_pgs = []
        self.listctrl_pgs = []
        self._make_week_pages()
        self._agpg_load()

    def click_button_settings(self, event):
        event.Skip()
        print('click_button_settings')

    def click_button_agpgget(self, event):
        self._agpg_get()

    def click_button_agpgreload(self, event):
        self._agpg_load()

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

    def run(self):
        self.Show()
        self.app.MainLoop()

    # private

    def _make_week_pages(self):
        for i in range(self.ONE_WEEK):
            panel_pg = wx.Panel(self.notebook_pgdates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sizer_pg = wx.BoxSizer(wx.VERTICAL)

            listctrl_pg = wx.ListCtrl(panel_pg, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
            listctrl_pg.AppendColumn(AGPG.Items.ID.name)
            listctrl_pg.AppendColumn(AGPG.Items.AIRTIME.name)
            listctrl_pg.AppendColumn(AGPG.Items.TITLE.name)
            listctrl_pg.AppendColumn(AGPG.Items.PERSONALITY.name)
            listctrl_pg.AppendColumn(AGPG.Items.DESCRIPTION.name)
            listctrl_pg.AppendColumn(AGPG.Items.REPEAT.name)
            listctrl_pg.AppendColumn(AGPG.Items.URL.name)
            sizer_pg.Add(listctrl_pg, 1, wx.ALL | wx.EXPAND, 0)

            panel_pg.SetSizer(sizer_pg)
            panel_pg.Layout()
            sizer_pg.Fit(panel_pg)
            self.notebook_pgdates.AddPage(panel_pg, f'{i+1}', False)

            self.panel_pgs.append(panel_pg)
            self.listctrl_pgs.append(listctrl_pg)

    def _agpg_get(self):
        for i in range(self.ONE_WEEK):
            date = datetime.date.today() + datetime.timedelta(days=i)
            self.agpg.save(self.agpg.get_by_day(date), f'{self.agpg.agpgs_dir}/{date.strftime(self.agpg.DATE_FORMAT)}.json')

    def _agpg_load(self):
        for i in range(self.ONE_WEEK):
            date = datetime.date.today() + datetime.timedelta(days=i)
            apgp = self.agpg.load(f'{self.agpg.agpgs_dir}/{date.strftime(self.agpg.DATE_FORMAT)}.json')
            self.notebook_pgdates.SetPageText(i, date.strftime('%m/%d'))
            self.listctrl_pgs[i].DeleteAllItems()
            for j, agpg in enumerate(apgp):
                self.listctrl_pgs[i].InsertItem(j, agpg[AGPG.Items.ID.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.AIRTIME.value,     f"{agpg[AGPG.Items.AIRTIME.name.lower()][0].strftime('%H:%M')} - {agpg[AGPG.Items.AIRTIME.name.lower()][1].strftime('%H:%M')}")
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.TITLE.value,       agpg[AGPG.Items.TITLE.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.PERSONALITY.value, agpg[AGPG.Items.PERSONALITY.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.DESCRIPTION.value, agpg[AGPG.Items.DESCRIPTION.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.REPEAT.value,      str(agpg[AGPG.Items.REPEAT.name.lower()]))
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.URL.value,         agpg[AGPG.Items.URL.name.lower()])

