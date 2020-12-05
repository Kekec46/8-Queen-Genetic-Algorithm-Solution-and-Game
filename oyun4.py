# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ornek4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from kaybetmek import*
from kazanmak import *

arr=[[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]
arr2=arr
olusan_kromozom=[0,0,0,0]
olusan_kromozom2=olusan_kromozom
class Ui_MainWindow4Oyun(object):
   
    
    def setup4Oyun(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button=[[0 for i in range(4)]for j in range(4)]
        self.kaydet_button = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_button.setGeometry(QtCore.QRect(40, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(65)
        self.kaydet_button.setFont(font)
        self.kaydet_button.setObjectName("kaydet_button")
        self.yeniden_button = QtWidgets.QPushButton(self.centralwidget)
        self.yeniden_button.setGeometry(QtCore.QRect(185, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(65)
        self.yeniden_button.setFont(font)
        self.yeniden_button.setObjectName("yeniden_button")
         
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
        self.button[0][0].clicked.connect(lambda:self.clicked1(0,0))
        self.button[0][1].clicked.connect(lambda:self.clicked1(0,1))
        self.button[0][2].clicked.connect(lambda:self.clicked1(0,2))
        self.button[0][3].clicked.connect(lambda:self.clicked1(0,3))
        self.button[1][0].clicked.connect(lambda:self.clicked1(1,0))
        self.button[1][1].clicked.connect(lambda:self.clicked1(1,1))
        self.button[1][2].clicked.connect(lambda:self.clicked1(1,2))
        self.button[1][3].clicked.connect(lambda:self.clicked1(1,3))
        self.button[2][0].clicked.connect(lambda:self.clicked1(2,0))
        self.button[2][1].clicked.connect(lambda:self.clicked1(2,1))
        self.button[2][2].clicked.connect(lambda:self.clicked1(2,2))
        self.button[2][3].clicked.connect(lambda:self.clicked1(2,3))
        self.button[3][0].clicked.connect(lambda:self.clicked1(3,0))
        self.button[3][1].clicked.connect(lambda:self.clicked1(3,1))
        self.button[3][2].clicked.connect(lambda:self.clicked1(3,2))
        self.button[3][3].clicked.connect(lambda:self.clicked1(3,3))
        self.kaydet_button.clicked.connect(lambda:self.kayit(MainWindow))
        self.yeniden_button.clicked.connect(lambda:self.yeni(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicked1(self,i,j):
         
        arr[i][j]=4-i
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
        
    def yeni(self,MainWindow):
        self.setup4Oyun(MainWindow)
        
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
        return int(6 - (yatay_cakisma + capraz_cakisma))
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "4x4 Game"))
        dosya=open("krom.txt","r")
        chrom_out= dosya.readline()
        self.kaydet_button.setText(_translate("MainWindow", "Play"))
        self.yeniden_button.setText(_translate("MainWindow", "Refresh"))
        for i in range(4):
            for j in range(4):
                self.button[i][j].setText(_translate("MainWindow", "X"))
        dizin=[1,2,3,4]
               
    def kayit(self,MainWindow):
        error=0
        #print(arr)
        for j in range(4):
            flag=0
            index=0
            for i in range(4):
                if ((arr[i][j]==1) or (arr[i][j]==2)  or (arr[i][j]==3) or (arr[i][j]==4)):
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
        if yeni_krom==6:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindowKaz()
            self.ui.setupKaz(self.window)
            self.window.show()
            
        else:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindowKay()
            self.ui.setupKay(self.window)
            self.window.show()
         
        for i in range(4):
            olusan_kromozom[i]=0
            for j in range(4):
                arr[i][j]=0 
                
        _translate = QtCore.QCoreApplication.translate
        for i in range(4):
            for j in range(4):
                self.button[i][j].setText(_translate("MainWindow", "X"))
         
        self.setup4Oyun(MainWindow)
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup4Oyun(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
