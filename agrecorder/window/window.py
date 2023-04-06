# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AGRecorder", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		sizer_base = wx.BoxSizer( wx.VERTICAL )

		self.panel_buttons = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_buttons = wx.BoxSizer( wx.HORIZONTAL )

		self.button_settings = wx.Button( self.panel_buttons, wx.ID_ANY, u"設定", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_settings, 0, wx.ALL, 5 )

		self.button_agpgget = wx.Button( self.panel_buttons, wx.ID_ANY, u"AGPG取得", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_agpgget, 0, wx.ALL, 5 )

		self.button_agpgreload = wx.Button( self.panel_buttons, wx.ID_ANY, u"AGPG再読み込み", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_agpgreload, 0, wx.ALL, 5 )

		self.button_immediatelyrecord = wx.Button( self.panel_buttons, wx.ID_ANY, u"即時録画", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_immediatelyrecord, 0, wx.ALL, 5 )

		self.button_play = wx.Button( self.panel_buttons, wx.ID_ANY, u"番組を視聴", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_play, 0, wx.ALL, 5 )

		self.button_exit = wx.Button( self.panel_buttons, wx.ID_ANY, u"終了", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizer_buttons.Add( self.button_exit, 0, wx.ALL, 5 )


		self.panel_buttons.SetSizer( sizer_buttons )
		self.panel_buttons.Layout()
		sizer_buttons.Fit( self.panel_buttons )
		sizer_base.Add( self.panel_buttons, 0, wx.ALL|wx.EXPAND, 0 )

		self.panel_notebook = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_notebook = wx.BoxSizer( wx.VERTICAL )

		self.notebook_contents = wx.Notebook( self.panel_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel_reservelist = wx.Panel( self.notebook_contents, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_reservelist = wx.BoxSizer( wx.HORIZONTAL )

		self.listctrl_reservelist = wx.ListCtrl( self.panel_reservelist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		sizer_reservelist.Add( self.listctrl_reservelist, 1, wx.ALL|wx.EXPAND, 5 )

		self.panel_reservebuttons = wx.Panel( self.panel_reservelist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_reservebuttons = wx.BoxSizer( wx.VERTICAL )

		self.button_reservedelete = wx.Button( self.panel_reservebuttons, wx.ID_ANY, u"削除", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		sizer_reservebuttons.Add( self.button_reservedelete, 0, wx.ALL, 5 )


		self.panel_reservebuttons.SetSizer( sizer_reservebuttons )
		self.panel_reservebuttons.Layout()
		sizer_reservebuttons.Fit( self.panel_reservebuttons )
		sizer_reservelist.Add( self.panel_reservebuttons, 0, wx.ALL|wx.EXPAND, 0 )


		self.panel_reservelist.SetSizer( sizer_reservelist )
		self.panel_reservelist.Layout()
		sizer_reservelist.Fit( self.panel_reservelist )
		self.notebook_contents.AddPage( self.panel_reservelist, u"予約一覧", True )
		self.panel_recordedlist = wx.Panel( self.notebook_contents, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_recordedlist = wx.BoxSizer( wx.HORIZONTAL )

		self.listctrl_recordedlist = wx.ListCtrl( self.panel_recordedlist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		sizer_recordedlist.Add( self.listctrl_recordedlist, 1, wx.ALL|wx.EXPAND, 5 )

		self.panel_recordedbuttons = wx.Panel( self.panel_recordedlist, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_recordedbuttons = wx.BoxSizer( wx.VERTICAL )

		self.button_recordedplay = wx.Button( self.panel_recordedbuttons, wx.ID_ANY, u"視聴", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		sizer_recordedbuttons.Add( self.button_recordedplay, 0, wx.ALL, 5 )

		self.button_recordeddelete = wx.Button( self.panel_recordedbuttons, wx.ID_ANY, u"削除", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		sizer_recordedbuttons.Add( self.button_recordeddelete, 0, wx.ALL, 5 )

		self.button_recordedopen = wx.Button( self.panel_recordedbuttons, wx.ID_ANY, u"保存先を開く", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		sizer_recordedbuttons.Add( self.button_recordedopen, 0, wx.ALL, 5 )


		self.panel_recordedbuttons.SetSizer( sizer_recordedbuttons )
		self.panel_recordedbuttons.Layout()
		sizer_recordedbuttons.Fit( self.panel_recordedbuttons )
		sizer_recordedlist.Add( self.panel_recordedbuttons, 0, wx.EXPAND |wx.ALL, 0 )


		self.panel_recordedlist.SetSizer( sizer_recordedlist )
		self.panel_recordedlist.Layout()
		sizer_recordedlist.Fit( self.panel_recordedlist )
		self.notebook_contents.AddPage( self.panel_recordedlist, u"録画一覧", False )
		self.panel_pg = wx.Panel( self.notebook_contents, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer_pg = wx.BoxSizer( wx.VERTICAL )

		self.notebook_pgdates = wx.Notebook( self.panel_pg, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		sizer_pg.Add( self.notebook_pgdates, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_pg.SetSizer( sizer_pg )
		self.panel_pg.Layout()
		sizer_pg.Fit( self.panel_pg )
		self.notebook_contents.AddPage( self.panel_pg, u"番組表", False )

		sizer_notebook.Add( self.notebook_contents, 1, wx.EXPAND |wx.ALL, 0 )


		self.panel_notebook.SetSizer( sizer_notebook )
		self.panel_notebook.Layout()
		sizer_notebook.Fit( self.panel_notebook )
		sizer_base.Add( self.panel_notebook, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( sizer_base )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_settings.Bind( wx.EVT_BUTTON, self.click_button_settings )
		self.button_agpgget.Bind( wx.EVT_BUTTON, self.click_button_agpgget )
		self.button_agpgreload.Bind( wx.EVT_BUTTON, self.click_button_agpgreload )
		self.button_immediatelyrecord.Bind( wx.EVT_BUTTON, self.click_button_immediatelyrecord )
		self.button_play.Bind( wx.EVT_BUTTON, self.click_button_play )
		self.button_exit.Bind( wx.EVT_BUTTON, self.click_button_exit )
		self.button_reservedelete.Bind( wx.EVT_BUTTON, self.click_button_reservedelete )
		self.button_recordedplay.Bind( wx.EVT_BUTTON, self.click_button_recordedplay )
		self.button_recordeddelete.Bind( wx.EVT_BUTTON, self.click_button_recordeddelete )
		self.button_recordedopen.Bind( wx.EVT_BUTTON, self.click_button_recordedopen )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def click_button_settings( self, event ):
		event.Skip()

	def click_button_agpgget( self, event ):
		event.Skip()

	def click_button_agpgreload( self, event ):
		event.Skip()

	def click_button_immediatelyrecord( self, event ):
		event.Skip()

	def click_button_play( self, event ):
		event.Skip()

	def click_button_exit( self, event ):
		event.Skip()

	def click_button_reservedelete( self, event ):
		event.Skip()

	def click_button_recordedplay( self, event ):
		event.Skip()

	def click_button_recordeddelete( self, event ):
		event.Skip()

	def click_button_recordedopen( self, event ):
		event.Skip()


