# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ornek4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setup4(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button=[[0 for i in range(4)]for j in range(4)]
        for j in range(4):
            for i in range(4):
                self.button[i][j] = QtWidgets.QPushButton(self.centralwidget)
                self.button[i][j].setGeometry(QtCore.QRect(j*80, i*80, 81, 81))
                self.button[i][j].setObjectName("button[i][j]")
                if ((i+1)%2==0 and (j+1)%2==0) or ((i)%2==0 and (j)%2==0):
                    self.button[i][j].setStyleSheet("background-color: brown")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "4x4 Sample"))
        dosya=open("krom.txt","r")
        chrom_out= dosya.readline()
        for i in range(4):
            for j in range(4):
                self.button[i][j].setText(_translate("MainWindow", "X"))
        dizin=[1,2,3,4]
        if chrom_out[0]=="S":
            for i in range(4):
                if chrom_out[i+1]=="1":
                    dizin[i]=1
                if chrom_out[i+1]=="2":
                    dizin[i]=2
                if chrom_out[i+1]=="3":
                    dizin[i]=3
                if chrom_out[i+1]=="4":
                    dizin[i]=4
                
            for i in range(4):
                self.button[4-dizin[i]][i].setText(_translate("MainWindow", "Q"))
                font = QtGui.QFont()
                font.setFamily("Uroob")
                font.setPointSize(25)
                font.setBold(True)
                font.setWeight(65)
                self.button[4-dizin[i]][i].setFont(font)
                self.button[4-dizin[i]][i].setStyleSheet("background-color: green")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
