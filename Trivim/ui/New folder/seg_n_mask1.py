# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seg_n_mask1.ui'
#
# Created: Thu Nov 27 12:50:35 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(664, 344)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bin_31/bin/isro.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(1.0)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 671, 352))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 40, 131, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(290, 280, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(310, 40, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 381, 211))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Trivim", None))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><img src=\":/new/prefix1/IIRSMAIN1.jpg\"/></p></body></html>", None))
        self.groupBox.setTitle(_translate("Dialog", "Segmentation", None))
        self.pushButton_4.setText(_translate("Dialog", "Image  Segmentation", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Image", None))
        self.label.setText(_translate("Dialog", "Select Image", None))
        self.pushButton.setText(_translate("Dialog", "Show Image", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Image Preview</span></p></body></html>", None))

import tt_rc
