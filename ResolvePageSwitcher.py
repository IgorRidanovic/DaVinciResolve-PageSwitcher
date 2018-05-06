#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve scripting proof of concept. Resolve page external switcher.
# Refer to Resolve V15 public beta 2 scripting API documentation for host setup.
# Copyright 2018 Igor Riđanović, www.hdhead.com

from PyQt4 import QtCore, QtGui
import DaVinciResolveScript

import sys
from threading import Thread

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8('Resolve Page Switcher'))
		Form.resize(561, 88)
		Form.setStyleSheet(_fromUtf8('background-color: #282828;'))

		self.horizontalLayout = QtGui.QHBoxLayout(Form)
		self.horizontalLayout.setObjectName(_fromUtf8('horizontalLayout'))
		self.mediaButton = QtGui.QPushButton(Form)
		self.mediaButton.setObjectName(_fromUtf8('mediaButton'))
		self.horizontalLayout.addWidget(self.mediaButton)
		self.editButton = QtGui.QPushButton(Form)
		self.editButton.setObjectName(_fromUtf8('editButton'))
		self.horizontalLayout.addWidget(self.editButton)
		self.fusionButton = QtGui.QPushButton(Form)
		self.fusionButton.setObjectName(_fromUtf8('fusionButton'))
		self.horizontalLayout.addWidget(self.fusionButton)
		self.colorButton = QtGui.QPushButton(Form)
		self.colorButton.setObjectName(_fromUtf8('colorButton'))
		self.horizontalLayout.addWidget(self.colorButton)
		self.fairlightButton = QtGui.QPushButton(Form)
		self.fairlightButton.setObjectName(_fromUtf8('fairlightButton'))
		self.horizontalLayout.addWidget(self.fairlightButton)
		self.deliverButton = QtGui.QPushButton(Form)
		self.deliverButton.setObjectName(_fromUtf8('deliverButton'))
		self.horizontalLayout.addWidget(self.deliverButton)
				
		self.mediaButton.clicked.connect(lambda: self.pageswitch('media'))
		self.editButton.clicked.connect(lambda: self.pageswitch('edit'))
		self.fusionButton.clicked.connect(lambda: self.pageswitch('fusion'))
		self.colorButton.clicked.connect(lambda: self.pageswitch('color'))
		self.fairlightButton.clicked.connect(lambda: self.pageswitch('fairlight'))
		self.deliverButton.clicked.connect(lambda: self.pageswitch('deliver'))
				
		self.mediaButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.editButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.fusionButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.colorButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.fairlightButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.deliverButton.setStyleSheet(_fromUtf8('background-color: #181818;\
													color: #929292;\
													border-color:\
													#555555; font-size: 13px;'\
													))
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate('Resolve Page Switcher', 'Resolve Page Switcher', None))
		self.mediaButton.setText(_translate('Form', 'Media', None))
		self.editButton.setText(_translate('Form', 'Edit', None))
		self.fusionButton.setText(_translate('Form', 'Fusion', None))
		self.colorButton.setText(_translate('Form', 'Color', None))
		self.fairlightButton.setText(_translate('Form', 'Fairlight', None))
		self.deliverButton.setText(_translate('Form', 'Deliver', None))

	# Start Resolve page flipping as a new thread
	def pageswitch(self, page):
		print page
		resolve.OpenPage(page)

if __name__ == '__main__':

	# Instantiate Resolve object
	resolve = DaVinciResolveScript.scriptapp('Resolve')

	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

