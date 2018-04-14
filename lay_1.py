# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from lay_2 import Ui_otherwindow
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

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_otherwindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1080, 727)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 20, 681))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1060, 10, 20, 681))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 0, 1051, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 680, 1051, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 50, 1001, 91))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 180, 141, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 180, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 250, 61, 25))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 250, 81, 25))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 250, 61, 25))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(390, 250, 71, 31))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 430, 21, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 250, 141, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(55, 291, 411, 361))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(620, 290, 361, 361))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 180, 41, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(780, 180, 41, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 80, 31, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 80, 31, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 80, 31, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 80, 31, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(720, 250, 171, 27))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuManage = QtGui.QMenu(self.menubar)
        self.menuManage.setObjectName(_fromUtf8("menuManage"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtGui.QAction(MainWindow)
        self.actionNew_Team.setObjectName(_fromUtf8("actionNew_Team"))
        self.actionOpen_Team = QtGui.QAction(MainWindow)
        self.actionOpen_Team.setObjectName(_fromUtf8("actionOpen_Team"))
        self.actionSave_Team = QtGui.QAction(MainWindow)
        self.actionSave_Team.setObjectName(_fromUtf8("actionSave_Team"))
        self.actionEvaluate_Team = QtGui.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName(_fromUtf8("actionEvaluate_Team"))
        self.menuManage.addAction(self.actionNew_Team)
        self.menuManage.addAction(self.actionOpen_Team)
        self.menuManage.addAction(self.actionSave_Team)
        self.menuManage.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QObject.connect(self.radioButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QObject.connect(self.radioButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.listView.doItemsLayout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Your Selections</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Batsmen (BAT)                       Bowlers (BOW)                 Allrounders (AR)                            Wicket-Keeper (WK)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Points Available", None))
        self.label_2.setText(_translate("MainWindow", "Points Used", None))
        self.radioButton.setText(_translate("MainWindow", "BAT", None))
        self.radioButton_2.setText(_translate("MainWindow", "BOW", None))
        self.radioButton_3.setText(_translate("MainWindow", "AR", None))
        self.radioButton_4.setText(_translate("MainWindow", "WK", None))
        self.label_3.setText(_translate("MainWindow", ">", None))
        self.label_4.setText(_translate("MainWindow", "Team Name", None))
        self.lineEdit.setText(_translate("MainWindow", "1000", None))
        self.lineEdit_2.setText(_translate("MainWindow", "1000", None))
        self.menuManage.setTitle(_translate("MainWindow", "Manage", None))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team", None))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team", None))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team", None))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team", None))
        self.actionEvaluate_Team.triggered.connect(self.openWindow)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

