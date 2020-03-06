# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import time
import os
import tkinter as tk
import shutil
import wx
import wx.xrc
from tkinter import filedialog
import win32con
import win32gui
import win32clipboard as w

import baiduTrans
import ocr_getstr
import screenshot

hwnd_title = []
hwnd_list = []
win_name = 'screenshot'

str_help = "使用说明：（建议不要一次性截取太多，因为分段可能错误）需要提取图片文字的，首先选择源语言，不选择默认中英文，使用载入图片按钮（或菜单，后同）或屏幕截图获取需要识别翻译的部分，按任意键完成截图，若识别结果不正确的部分的可以在左侧文本框内进行修正。修正完成后选择源语言和目标语言，点击翻译原文完成翻译，翻译完成后可点击复制结果将翻译后的结果复制到粘贴板，以便其他应用使用"

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		if not os.path.exists('workspace'):
			os.mkdir('workspace')
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "截屏翻译工具", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		self.icon1=wx.Icon(name="favicon.ico",type=wx.BITMAP_TYPE_ICO)
		self.SetIcon(self.icon1)
		self.SetSizeHints( wx.Size( 1080,720 ), wx.Size( 1080,720 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel91 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19.Add( self.m_panel91, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.src_info = wx.TextCtrl( self, wx.ID_ANY, u"请在此处选择源语言", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.BORDER_NONE )
		bSizer24.Add( self.src_info, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( bSizer24, 3, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		#中 英 法 西 葡 意 德 日 韩

		src_choiceChoices = [ u"Auto-自动检测", u"Chinese-中文", u"English-英语", u"French-法语", u"Spanish-西语",u"Portuguese-葡语",u"Italian-意语", u"Germany-德语", u"Japanese-日语",u"Korean-韩语" ]
		self.src_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, src_choiceChoices, 0 )
		self.src_choice.SetSelection( 0 )
		bSizer25.Add( self.src_choice, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer20.Add( bSizer25, 2, wx.EXPAND, 5 )


		bSizer18.Add( bSizer20, 5, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer21, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.dst_info = wx.TextCtrl( self, wx.ID_ANY, u"请在此处选择目标语言", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.BORDER_NONE )
		bSizer26.Add( self.dst_info, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer26, 3, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		dst_choiceChoices = [ u"Chinese-中文", u"English-英语", u"French-法语", u"Spanish-西语",u"Portuguese-葡语",u"Italian-意语", u"Germany-德语", u"Japanese-日语",u"Korean-韩语" ]
		self.dst_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, dst_choiceChoices, 0 )
		self.dst_choice.SetSelection( 1 )
		bSizer27.Add( self.dst_choice, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( bSizer27, 2, wx.EXPAND, 5 )


		bSizer18.Add( bSizer22, 5, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer23.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer23, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 2, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.src_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer8.Add( self.src_text, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer8, 6, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.dst_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer10.Add( self.dst_text, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer10, 6, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 8, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.load_btn = wx.Button( self, wx.ID_ANY, u"载入图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.load_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer13, 2, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.sc_btn = wx.Button( self, wx.ID_ANY, u"屏幕截图", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.sc_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer15, 2, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.trans_btn = wx.Button( self, wx.ID_ANY, u"翻译原文", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.trans_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer28, 2, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer29, 1, wx.EXPAND, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.copy_btn = wx.Button( self, wx.ID_ANY, u"复制结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.copy_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer30, 2, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.exit_btn = wx.Button( self, wx.ID_ANY, u"关闭程序", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.exit_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer35, 2, wx.EXPAND, 5 )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel171 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37.Add( self.m_panel171, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer33.Add( bSizer37, 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.info_text = wx.TextCtrl( self, wx.ID_ANY, u"使用说明：（建议不要一次性截取太多，因为分段可能错误）需要提取图片文字的，首先选择源语言，不选择默认中英文，使用载入图片按钮（或菜单，后同）或屏幕截图获取需要识别翻译的部分，按任意键完成截图，若识别结果不正确的部分的可以在左侧文本框内进行修正。修正完成后选择源语言和目标语言，点击翻译原文完成翻译，翻译完成后可点击复制结果将翻译后的结果复制到粘贴板，以便其他应用使用", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_READONLY|wx.BORDER_NONE )
		self.info_text.SetMaxSize( wx.Size( -1,80 ) )

		bSizer40.Add( self.info_text, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer40, 15, wx.EXPAND, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel181 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38.Add( self.m_panel181, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer33.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer6.Add( bSizer33, 4, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( bSizer34, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 2, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.run_menu = wx.Menu()
		self.load_menu = wx.MenuItem( self.run_menu, wx.ID_ANY, u"Load Image", wx.EmptyString, wx.ITEM_NORMAL )
		self.run_menu.Append( self.load_menu )

		self.sc_menu = wx.MenuItem( self.run_menu, wx.ID_ANY, u"Screenshot", wx.EmptyString, wx.ITEM_NORMAL )
		self.run_menu.Append( self.sc_menu )

		self.trans_menu = wx.MenuItem( self.run_menu, wx.ID_ANY, u"Translate", wx.EmptyString, wx.ITEM_NORMAL )
		self.run_menu.Append( self.trans_menu )

		self.copy_menu = wx.MenuItem( self.run_menu, wx.ID_ANY, u"Copy Result", wx.EmptyString, wx.ITEM_NORMAL )
		self.run_menu.Append( self.copy_menu )

		self.exit_menu = wx.MenuItem( self.run_menu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.run_menu.Append( self.exit_menu )

		self.m_menubar1.Append( self.run_menu, u"Run" )

		self.About_menu = wx.Menu()
		self.about_menu = wx.MenuItem( self.About_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.About_menu.Append( self.about_menu )

		self.m_menubar1.Append( self.About_menu, u"About" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.load_btn.Bind( wx.EVT_BUTTON, self.load_btnOnButtonClick )
		self.sc_btn.Bind( wx.EVT_BUTTON, self.sc_btnOnButtonClick )
		self.trans_btn.Bind( wx.EVT_BUTTON, self.trans_btnOnButtonClick )
		self.copy_btn.Bind( wx.EVT_BUTTON, self.copy_btnOnButtonClick )
		self.exit_btn.Bind( wx.EVT_BUTTON, self.exit_btnOnButtonClick )
		self.Bind( wx.EVT_MENU, self.load_menuOnMenuSelection, id = self.load_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.sc_menuOnMenuSelection, id = self.sc_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.trans_menuOnMenuSelection, id = self.trans_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.copy_menuOnMenuSelection, id = self.copy_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.exit_menuOnMenuSelection, id = self.exit_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.about_menuOnMenuSelection, id = self.about_menu.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def load_btnOnButtonClick( self, event ):
		self.info_text.SetValue(str_help)
		self.src_text.Clear()
		self.dst_text.Clear()
		#load image
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()
		despath = 'workspace/1.png'
		# shutil.move(file_path,despath)
		shutil.copy2(file_path,despath)
		time.sleep(0.5)
		lang_list = ['CHN_ENG','CHN_ENG','ENG','FRE','SPA','POR','ITA','GER','JAP','KOR']
		lang = lang_list[self.src_choice.GetSelection()]
		src_str = ocr_getstr.run(lang)
		self.src_text.SetValue(src_str)
		event.Skip()

	def sc_btnOnButtonClick( self, event ):
		self.src_text.Clear()
		self.dst_text.Clear()
		self.info_text.SetValue(str_help)
		self.Iconize(True)
		time.sleep(0.5)
		# self.Hide()
		screenshot.take_screenshot()
		#get screenshot and get the chars
		if os.path.exists('workspace/1.png'):
			self.Iconize(False)
			# self.Show()
		lang_list = ['CHN_ENG','CHN_ENG','ENG','FRE','SPA','POR','ITA','GER','JAP','KOR']
		lang = lang_list[self.src_choice.GetSelection()]
		src_str = ocr_getstr.run(lang)
		self.src_text.SetValue(src_str)
		event.Skip()

	def trans_btnOnButtonClick( self, event ):
		self.dst_text.Clear()
		self.info_text.SetValue(str_help)
		src_lang_list = ['auto','zh','en','fra','spa','pt','it','de','jp','kor']
		dst_lang_list = ['zh','en','fra','spa','pt','it','de','jp','kor']
		src_lang = src_lang_list[self.src_choice.GetSelection()]
		dest_lang = dst_lang_list[self.dst_choice.GetSelection()]
		query_text = self.src_text.GetValue()
		result_str = baiduTrans.trans_get(src_lang,dest_lang,query_text)
		self.dst_text.SetValue(result_str)
		event.Skip()

	def copy_btnOnButtonClick( self, event ):
		self.info_text.SetValue(str_help)
		str_cb = self.dst_text.GetValue()
		w.OpenClipboard()
		w.EmptyClipboard()
		w.SetClipboardData(win32con.CF_UNICODETEXT,str_cb)
		w.CloseClipboard()
		self.info_text.SetValue("已复制到剪切板")
		event.Skip()

	def exit_btnOnButtonClick( self, event ):
		self.Close()
		event.Skip()

	def load_menuOnMenuSelection( self, event ):
		self.info_text.SetValue(str_help)
		self.src_text.Clear()
		self.dst_text.Clear()
		#load image
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()
		despath = 'workspace/1.png'
		# shutil.move(file_path,despath)
		shutil.copy2(file_path,despath)
		time.sleep(0.5)
		lang_list = ['CHN_ENG','CHN_ENG','ENG','FRE','SPA','POR','ITA','GER','JAP','KOR']
		lang = lang_list[self.src_choice.GetSelection()]
		src_str = ocr_getstr.run(lang)
		self.src_text.SetValue(src_str)
		event.Skip()

	def sc_menuOnMenuSelection( self, event ):
		self.src_text.Clear()
		self.dst_text.Clear()
		self.info_text.SetValue(str_help)
		self.Iconize(True)
		time.sleep(0.5)
		# self.Hide()
		hide_windows()
		screenshot.take_screenshot()
		
		#get screenshot and get the chars
		if os.path.exists('workspace/1.png'):
			self.Iconize(False)
			# self.Show()
		lang_list = ['CHN_ENG','CHN_ENG','ENG','FRE','SPA','POR','ITA','GER','JAP','KOR']
		lang = lang_list[self.src_choice.GetSelection()]
		src_str = ocr_getstr.run(lang)
		self.src_text.SetValue(src_str)
		event.Skip()

	def trans_menuOnMenuSelection( self, event ):
		self.dst_text.Clear()
		self.info_text.SetValue(str_help)
		src_lang_list = ['auto','zh','en','fra','spa','pt','it','de','jp','kor']
		dst_lang_list = ['zh','en','fra','spa','pt','it','de','jp','kor']
		src_lang = src_lang_list[self.src_choice.GetSelection()]
		dest_lang = dst_lang_list[self.dst_choice.GetSelection()]
		query_text = self.src_text.GetValue()
		result_str = baiduTrans.trans_get(src_lang,dest_lang,query_text)
		self.dst_text.SetValue(result_str)
		event.Skip()

	def copy_menuOnMenuSelection( self, event ):
		self.info_text.SetValue(str_help)
		str_cb = self.dst_text.GetValue()
		w.OpenClipboard()
		w.EmptyClipboard()
		w.SetClipboardData(win32con.CF_UNICODETEXT,str_cb)
		w.CloseClipboard()
		self.info_text.SetValue("已复制到剪切板")
		event.Skip()

	def exit_menuOnMenuSelection( self, event ):
		self.Close()
		event.Skip()

	def about_menuOnMenuSelection( self, event ):
		str_about = 'Author: Norman Guan, E-mail: 1157411076@qq.com, Github: github.com/textGuan, webpage: jyyj.fun\n 使用百度翻译API及百度文字提取SDK'
		self.info_text.SetValue(str_about)
		event.Skip()
			

