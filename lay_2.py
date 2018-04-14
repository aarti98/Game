# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_otherwindow(object):
    def setupUi(self, otherwindow):
        otherwindow.setObjectName(_fromUtf8("otherwindow"))
        otherwindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(otherwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 301, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 741, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.list1 = QtGui.QListWidget(self.centralwidget)
        self.list1.setGeometry(QtCore.QRect(30, 110, 311, 371))
        self.list1.setObjectName(_fromUtf8("list1"))
        self.list2 = QtGui.QListWidget(self.centralwidget)
        self.list2.setGeometry(QtCore.QRect(465, 110, 301, 371))
        self.list2.setObjectName(_fromUtf8("list2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 280, 31, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 70, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 70, 51, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.points_evaluate = QtGui.QLineEdit(self.centralwidget)
        self.points_evaluate.setGeometry(QtCore.QRect(570, 70, 51, 27))
        self.points_evaluate.setObjectName(_fromUtf8("points_evaluate"))
        self.score_cal = QtGui.QPushButton(self.centralwidget)
        self.score_cal.setGeometry(QtCore.QRect(340, 500, 121, 27))
        self.score_cal.setObjectName(_fromUtf8("score_cal"))
        otherwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(otherwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        otherwindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(otherwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        otherwindow.setStatusBar(self.statusbar)

        self.retranslateUi(otherwindow)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def retranslateUi(self, otherwindow):
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow", None))
        self.label.setText(_translate("otherwindow", "Evaluate performance of your Fantasy Team", None))
        self.label_2.setText(_translate("otherwindow", "==>", None))
        self.label_3.setText(_translate("otherwindow", "Players", None))
        self.label_4.setText(_translate("otherwindow", "Points:", None))
        self.score_cal.setText(_translate("otherwindow", "Calculate Score", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    otherwindow = QtGui.QMainWindow()
    ui = Ui_otherwindow()
    ui.setupUi(otherwindow)
    otherwindow.show()
    sys.exit(app.exec_())

