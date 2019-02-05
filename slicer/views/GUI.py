# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CFRP Slicer", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer_Base_Setting = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Base Setting" ), wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer_Filament_diameter = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"Filament diameter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Filament_diameter.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, wx.EmptyString, style=wx.TE_RIGHT)
		bSizer_Filament_diameter.Add( self.m_textCtrl1, 1, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Filament_diameter.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer_Filament_diameter, 0, 0, 5 )

		bSizer_Nozzle_diameter = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"Nozzle diameter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Nozzle_diameter.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, wx.EmptyString, style=wx.TE_RIGHT )
		bSizer_Nozzle_diameter.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Nozzle_diameter.Add( self.m_staticText4, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer_Nozzle_diameter, 0, 0, 50 )

		bSizer_Nozzle_temperature = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"Nozzle temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Nozzle_temperature.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, wx.EmptyString, style=wx.TE_RIGHT )
		bSizer_Nozzle_temperature.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"℃", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Nozzle_temperature.Add( self.m_staticText6, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer_Nozzle_temperature, 0, 0, 5 )

		bSizer_Bet_temperature = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"Bet temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Bet_temperature.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, wx.EmptyString, style=wx.TE_RIGHT )
		bSizer_Bet_temperature.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"℃", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_Bet_temperature.Add( self.m_staticText8, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer_Bet_temperature, 0, 0, 5 )

		bSizer_print_speed = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"Print speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_print_speed.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, wx.EmptyString, style=wx.TE_RIGHT )
		bSizer_print_speed.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( sbSizer_Base_Setting.GetStaticBox(), wx.ID_ANY, u"mm/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer_print_speed.Add( self.m_staticText10, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer_print_speed, 0, wx.EXPAND, 5 )


		sbSizer_Base_Setting.Add( bSizer2, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( sbSizer_Base_Setting )
		self.m_panel1.Layout()
		sbSizer_Base_Setting.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer_Print_pattern = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Print Pattern" ), wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer_surround_outer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, u"Surround outer frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer_surround_outer.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 3, 0 )
		bSizer_surround_outer.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, u"times", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer_surround_outer.Add( self.m_staticText12, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer_surround_outer, 0, wx.EXPAND, 5 )

		bSizer_surround_inner = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, u"Surround inner ring", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer_surround_inner.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 3, 0 )
		bSizer_surround_inner.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( sbSizer_Print_pattern.GetStaticBox(), wx.ID_ANY, u"times", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer_surround_inner.Add( self.m_staticText14, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer_surround_inner, 0, wx.EXPAND, 5 )


		sbSizer_Print_pattern.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( sbSizer_Print_pattern )
		self.m_panel2.Layout()
		sbSizer_Print_pattern.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND, 5 )

		bSizer_button = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_import = wx.Button( self, wx.ID_ANY, u"Import file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_button.Add( self.m_button_import, 0, wx.ALL, 5 )

		self.m_button_convert = wx.Button( self, wx.ID_ANY, u"Convert G-code", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_button.Add( self.m_button_convert, 0, wx.ALL, 5 )

		self.m_button_save_as = wx.Button( self, wx.ID_ANY, u"Save as...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_button.Add( self.m_button_save_as, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer_button, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl1.Bind( wx.EVT_TEXT, self.filament_diameter_value )
		self.m_textCtrl2.Bind( wx.EVT_TEXT, self.nozzle_diameter_value )
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.nozzle_temperature_value )
		self.m_textCtrl4.Bind( wx.EVT_TEXT, self.Bet_temperature_value )
		self.m_textCtrl5.Bind( wx.EVT_TEXT, self.print_spped_value )
		self.m_spinCtrl1.Bind( wx.EVT_TEXT, self.surround_outer_ctrl )
		self.m_spinCtrl2.Bind( wx.EVT_TEXT, self.surround_inner_ctrl )
		self.m_button_import.Bind( wx.EVT_BUTTON, self.import_file )
		self.m_button_convert.Bind( wx.EVT_BUTTON, self.convert_gcode )
		self.m_button_save_as.Bind( wx.EVT_BUTTON, self.save_as )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filament_diameter_value( self, event ):
		event.Skip()

	def nozzle_diameter_value( self, event ):
		event.Skip()

	def nozzle_temperature_value( self, event ):
		event.Skip()

	def Bet_temperature_value( self, event ):
		event.Skip()

	def print_spped_value( self, event ):
		event.Skip()

	def surround_outer_ctrl( self, event ):
		event.Skip()

	def surround_inner_ctrl( self, event ):
		event.Skip()

	def import_file( self, event ):
		event.Skip()

	def convert_gcode( self, event ):
		event.Skip()

	def save_as( self, event ):
		event.Skip()


