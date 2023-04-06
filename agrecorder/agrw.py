# wx
import wx

# window
from window.window import Window


# ag record window
class AGRW(Window):

    # public

    def __init__(self, parent):
        super().__init__(parent)

        # 1週間分のページを作成
        self.panel_pgs = []
        self.listctrl_pg = []

        for i in range(7):
            panel_pg = wx.Panel(self.notebook_pgdates, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            sizer_pg = wx.BoxSizer(wx.VERTICAL)

            listctrl_pg = wx.ListCtrl(panel_pg, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
            sizer_pg.Add(listctrl_pg, 1, wx.ALL | wx.EXPAND, 0)

            panel_pg.SetSizer(sizer_pg)
            panel_pg.Layout()
            sizer_pg.Fit(panel_pg)
            self.notebook_pgdates.AddPage(panel_pg, f'{i+1}', False)

            self.panel_pgs.append(panel_pg)
            self.listctrl_pg.append(listctrl_pg)

    def click_button_settings(self, event):
        event.Skip()
        print('click_button_settings')

    def click_button_agpgget(self, event):
        event.Skip()
        print('click_button_agpgget')

    def click_button_agpgreload(self, event):
        event.Skip()
        print('click_button_agpgreload')

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

