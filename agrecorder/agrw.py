# standard
import datetime
import threading

# wx
import wx

# agconfig agpg, agrp
from agrecorder.agconfig import AGConfig
from agrecorder.agpg import AGPG
from agrecorder.agrp import AGRP
from agrecorder.agutil import AGUtil
# window
from agrecorder.window.window import Window


# ag record window
class AGRW(Window):

    # public

    ONE_WEEK = 7

    def __init__(self, config_path: str):
        self.app = wx.App()
        super().__init__(None)
        self._agconfig = AGConfig(config_path)
        self.agrp = AGRP(self._agconfig)

        # 1週間分のページを作成
        self.agpgs = []
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
        self.agrp.download()

    def click_button_play(self, event):
        self.agrp.play()

    def click_button_exit(self, event):
        self.agrp.stop()
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
        #thread = threading.Thread(target=self._background)
        self.Show()
        self.app.MainLoop()

    # private

    def _background(self):
        #TODO: update agpg every 1 day
        pass

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
        #TODO: more efficiently
        self.agpgs.clear()
        for i in range(self.ONE_WEEK):
            agpg = AGPG(self._agconfig, datetime.date.today() + datetime.timedelta(days=i))
            agpg.get_by_day()
            agpg.save()
            self.agpgs.append(agpg)

    def _agpg_load(self):
        self.agpgs.clear()
        for i in range(self.ONE_WEEK):
            date = datetime.date.today() + datetime.timedelta(days=i)
            self.notebook_pgdates.SetPageText(i, date.strftime('%m/%d'))
            self.listctrl_pgs[i].DeleteAllItems()
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.ID.value,          50)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.AIRTIME.value,     80)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.TITLE.value,       200)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.PERSONALITY.value, 100)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.DESCRIPTION.value, 250)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.REPEAT.value,      60)
            self.listctrl_pgs[i].SetColumnWidth(AGPG.Items.URL.value,         200)
            agpg = AGPG(self._agconfig, datetime.date.today() + datetime.timedelta(days=i))
            self.agpgs.append(agpg)
            for j, agpg in enumerate(agpg.load()):
                self.listctrl_pgs[i].InsertItem(j, agpg[AGPG.Items.ID.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.AIRTIME.value,     f"{agpg[AGPG.Items.AIRTIME.name.lower()][0].strftime('%H:%M')} - {agpg[AGPG.Items.AIRTIME.name.lower()][1].strftime('%H:%M')}")
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.TITLE.value,       agpg[AGPG.Items.TITLE.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.PERSONALITY.value, agpg[AGPG.Items.PERSONALITY.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.DESCRIPTION.value, agpg[AGPG.Items.DESCRIPTION.name.lower()])
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.REPEAT.value,      str(agpg[AGPG.Items.REPEAT.name.lower()]))
                self.listctrl_pgs[i].SetItem(j, AGPG.Items.URL.value,         agpg[AGPG.Items.URL.name.lower()])

