# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oyun7.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from kaybetmek import*
from kazanmak import *

arr=[[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]]
arr2=arr
olusan_kromozom=[0,0,0,0,0,0,0]
olusan_kromozom2=olusan_kromozom

class Ui_MainWindow7Oyun(object):
   
    
    def setup7Oyun(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button=[[0 for i in range(7)]for j in range(7)]
        self.kaydet_button = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_button.setGeometry(QtCore.QRect(140, 600, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(65)
        self.kaydet_button.setFont(font)
        self.kaydet_button.setObjectName("kaydet_button")
        self.yeniden_button = QtWidgets.QPushButton(self.centralwidget)
        self.yeniden_button.setGeometry(QtCore.QRect(328, 600, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(65)
        self.yeniden_button.setFont(font)
        self.yeniden_button.setObjectName("yeniden_button")
        
         
        for j in range(7):
            for i in range(7):
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
        self.button[0][0].clicked.connect(lambda:self.clicked1(0,0))
        self.button[0][1].clicked.connect(lambda:self.clicked1(0,1))
        self.button[0][2].clicked.connect(lambda:self.clicked1(0,2))
        self.button[0][3].clicked.connect(lambda:self.clicked1(0,3))
        self.button[0][4].clicked.connect(lambda:self.clicked1(0,4))
        self.button[0][5].clicked.connect(lambda:self.clicked1(0,5))
        self.button[0][6].clicked.connect(lambda:self.clicked1(0,6))
        self.button[1][0].clicked.connect(lambda:self.clicked1(1,0))
        self.button[1][1].clicked.connect(lambda:self.clicked1(1,1))
        self.button[1][2].clicked.connect(lambda:self.clicked1(1,2))
        self.button[1][3].clicked.connect(lambda:self.clicked1(1,3))
        self.button[1][4].clicked.connect(lambda:self.clicked1(1,4))
        self.button[1][5].clicked.connect(lambda:self.clicked1(1,5))
        self.button[1][6].clicked.connect(lambda:self.clicked1(1,6))
        self.button[2][0].clicked.connect(lambda:self.clicked1(2,0))
        self.button[2][1].clicked.connect(lambda:self.clicked1(2,1))
        self.button[2][2].clicked.connect(lambda:self.clicked1(2,2))
        self.button[2][3].clicked.connect(lambda:self.clicked1(2,3))
        self.button[2][4].clicked.connect(lambda:self.clicked1(2,4))
        self.button[2][5].clicked.connect(lambda:self.clicked1(2,5))
        self.button[2][6].clicked.connect(lambda:self.clicked1(2,6))
        self.button[3][0].clicked.connect(lambda:self.clicked1(3,0))
        self.button[3][1].clicked.connect(lambda:self.clicked1(3,1))
        self.button[3][2].clicked.connect(lambda:self.clicked1(3,2))
        self.button[3][3].clicked.connect(lambda:self.clicked1(3,3))
        self.button[3][4].clicked.connect(lambda:self.clicked1(3,4))
        self.button[3][5].clicked.connect(lambda:self.clicked1(3,5))
        self.button[3][6].clicked.connect(lambda:self.clicked1(3,6))
        self.button[4][0].clicked.connect(lambda:self.clicked1(4,0))
        self.button[4][1].clicked.connect(lambda:self.clicked1(4,1))
        self.button[4][2].clicked.connect(lambda:self.clicked1(4,2))
        self.button[4][3].clicked.connect(lambda:self.clicked1(4,3))
        self.button[4][4].clicked.connect(lambda:self.clicked1(4,4))
        self.button[4][5].clicked.connect(lambda:self.clicked1(4,5))
        self.button[4][6].clicked.connect(lambda:self.clicked1(4,6))
        self.button[5][0].clicked.connect(lambda:self.clicked1(5,0))
        self.button[5][1].clicked.connect(lambda:self.clicked1(5,1))
        self.button[5][2].clicked.connect(lambda:self.clicked1(5,2))
        self.button[5][3].clicked.connect(lambda:self.clicked1(5,3))
        self.button[5][4].clicked.connect(lambda:self.clicked1(5,4))
        self.button[5][5].clicked.connect(lambda:self.clicked1(5,5))
        self.button[5][6].clicked.connect(lambda:self.clicked1(5,6))
        self.button[6][0].clicked.connect(lambda:self.clicked1(6,0))
        self.button[6][1].clicked.connect(lambda:self.clicked1(6,1))
        self.button[6][2].clicked.connect(lambda:self.clicked1(6,2))
        self.button[6][3].clicked.connect(lambda:self.clicked1(6,3))
        self.button[6][4].clicked.connect(lambda:self.clicked1(6,4))
        self.button[6][5].clicked.connect(lambda:self.clicked1(6,5))
        self.button[6][6].clicked.connect(lambda:self.clicked1(6,6))
        
        self.kaydet_button.clicked.connect(lambda:self.kayit(MainWindow))
        self.yeniden_button.clicked.connect(lambda:self.yeni(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def yeni(self,MainWindow):
        self.setup7Oyun(MainWindow)
    
    
    def clicked1(self,i,j):
         
        arr[i][j]=7-i
        _translate = QtCore.QCoreApplication.translate
        self.button[i][j].setText(_translate("MainWindow", "Q"))
        print("Basılan Bölge Değeri: {} ".format(arr[i][j]))
        self.button[i][j].setStyleSheet("background-color: green")
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.button[i][j].setFont(font)
        
    def controls(self,kromozom):
        yatay_cakisma= sum([kromozom.count(queen)-1 for queen in kromozom])/2
        capraz_cakisma = 0

        uzunluk = len(kromozom)
        sol_x = [0] * 2*uzunluk
        sag_x = [0] * 2*uzunluk
        for i in range(uzunluk):
            sol_x[i + kromozom[i] - 1] += 1
            sag_x[len(kromozom) - i + kromozom[i] - 2] += 1
        capraz_cakisma = 0
        for i in range(2*uzunluk-1):
            flag = 0
            if sol_x[i] > 1:
                flag += sol_x[i]-1
            if sag_x[i] > 1:
                flag += sag_x[i]-1
            capraz_cakisma += flag / (uzunluk-abs(i-uzunluk+1))   
        return int(21 - (yatay_cakisma + capraz_cakisma))
    
    def kayit(self,MainWindow):
        error=0
        #print(arr)
        for j in range(7):
            flag=0
            index=0
            for i in range(7):
                if ((arr[i][j]==1) or (arr[i][j]==2)  or (arr[i][j]==3) or (arr[i][j]==4) or (arr[i][j]==5) or (arr[i][j]==6) or (arr[i][j]==7)):
                    flag+=1
                    
                    if flag==1:
                        index=arr[i][j]
                        olusan_kromozom[j]=index
                    else:
                        error+=1
                        break
            if (error==1):
                 break
        print("Oluşan Koromozom: {} ".format(olusan_kromozom))
        yeni_krom=self.controls(olusan_kromozom)
        if yeni_krom==21:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindowKaz()
            self.ui.setupKaz(self.window)
            self.window.show()
            
        else:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindowKay()
            self.ui.setupKay(self.window)
            self.window.show()
         
        for i in range(7):
            olusan_kromozom[i]=0
            for j in range(7):
                arr[i][j]=0 
                
        _translate = QtCore.QCoreApplication.translate
        for i in range(7):
            for j in range(7):
                self.button[i][j].setText(_translate("MainWindow", "X"))
            
        self.setup7Oyun(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "7x7 Game"))
        dosya=open("krom.txt","r")
        chrom_out= dosya.readline()
        self.kaydet_button.setText(_translate("MainWindow", "Play"))
        self.yeniden_button.setText(_translate("MainWindow", "Refresh"))
        for i in range(7):
            for j in range(7):
                self.button[i][j].setText(_translate("MainWindow", "X"))
        dizin=[1,2,3,4,5,6,7]
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup7Oyun(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
