import random
from anasayfa import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ornek8 import *
from ornek7 import *
from ornek6 import *
from ornek5 import *
from ornek4 import *
from oyun4 import *
from oyun5 import *
from oyun6 import *
from oyun7 import *
from oyun8 import *
import sys

class Ui_MainWindow(object):
    def oyun8bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow8Oyun()
        self.ui.setup8Oyun(self.window)
        self.window.show()
    def oyun7bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow7Oyun()
        self.ui.setup7Oyun(self.window)
        self.window.show()
    def oyun6bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow6Oyun()
        self.ui.setup6Oyun(self.window)
        self.window.show()
    def oyun5bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow5Oyun()
        self.ui.setup5Oyun(self.window)
        self.window.show()
    def oyun4bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4Oyun()
        self.ui.setup4Oyun(self.window)
        self.window.show()
    def ornek8bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow8()
        self.ui.setup8(self.window)
        self.window.show()
    def ornek7bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow7()
        self.ui.setup7(self.window)
        self.window.show()
    def ornek6bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow6()
        self.ui.setup6(self.window)
        self.window.show()
    def ornek5bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow5()
        self.ui.setup5(self.window)
        self.window.show()
    def ornek4bas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4()
        self.ui.setup4(self.window)
        self.window.show()
        
    def noyun(self):
        content=self.comboBox.currentText()
        dosya=open("krom.txt","w")
        dosya.write("O"+content)
        dosya.write("Oww")
        dosya.close()
        if content=="8":
            self.oyun8bas()
        if content=="7":
            self.oyun7bas()
        if content=="6":
            self.oyun6bas()
        if content=="5":
            self.oyun5bas()
        if content=="4":
            self.oyun4bas()
            
    def nsayisi(self):
        content=self.comboBox.currentText()
        chess_genetic(content)
        if content=="8":
            self.ornek8bas()
        if content=="7":
            self.ornek7bas()
        if content=="6":
            self.ornek6bas()
        if content=="5":
            self.ornek5bas()
        if content=="4":
            self.ornek4bas()
    def inputn(self):
         return self.comboBox.currentText()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oyun_buton = QtWidgets.QPushButton(self.centralwidget)
        self.oyun_buton.setGeometry(QtCore.QRect(50, 14, 231, 331))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(115)
        self.oyun_buton.setFont(font)
        self.oyun_buton.setObjectName("oyun_buton")
        self.oyun_buton.setStyleSheet("background-image : url(oyna.jpg); color :indigo")
        self.oyun_buton.clicked.connect(self.noyun)
        self.ornek_buton = QtWidgets.QPushButton(self.centralwidget)
        self.ornek_buton.setGeometry(QtCore.QRect(308, 14, 241, 331))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(115)      
        self.ornek_buton.setFont(font)
        self.ornek_buton.setObjectName("ornek_buton")
        self.ornek_buton.setStyleSheet("background-image : url(aynali.jpg); color : gold")
        self.ornek_buton.clicked.connect(self.nsayisi)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(147, 360, 150, 31))
        self.label.setObjectName("label")
        self.labelad = QtWidgets.QLabel(self.centralwidget)
        self.labelad.setGeometry(QtCore.QRect(420, 410, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(65)
        self.labelad.setFont(font) 
        self.labelad.setObjectName("labelad")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 362, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8 Queen "))
        self.oyun_buton.setText(_translate("MainWindow", "Game"))
        self.ornek_buton.setText(_translate("MainWindow", "Example"))
        self.label.setText(_translate("MainWindow", "Board Size (NxN): N="))
        self.labelad.setText(_translate("MainWindow", "Developer \U0001F469\u200D\U0001F4BB Mehmet KEKEC "))
        self.comboBox.setItemText(0, _translate("MainWindow", "4"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "7"))
        self.comboBox.setItemText(4, _translate("MainWindow", "8"))
        
def chess_genetic(number):

    def rnd_kromozom(size):  
        return [ random.randint(1, nq) for _ in range(nq) ]

    def controls(kromozom):
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
        return int(max_c - (yatay_cakisma + capraz_cakisma)) 

    def olasilik_hesabi(kromozom, controls):
        return controls(kromozom) / max_c

    def rnd_top(populasyon, ihtimaller):
        ihtimal = zip(populasyon, ihtimaller)
        total = sum(w for c, w in ihtimal)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(populasyon, ihtimaller):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Burada yok"
        
    def caprazlama(k1, k2): 
        k_uzunluk = len(k1)
        rnd = random.randint(0, k_uzunluk - 1)
        return k1[0:rnd] + k2[rnd:k_uzunluk]

    def mutasyon(k_index):  
        k_uzunluk = len(k_index)
        rnd = random.randint(0, k_uzunluk - 1)
        rnd1 = random.randint(1, k_uzunluk)
        k_index[rnd] = rnd1
        return k_index

    def vezir_gen(populasyon, controls):
        if(nq==4 and nq==5):
            mutasyon_ihtimali = 0.1
        else:
            mutasyon_ihtimali = 0.5
        arr_yeni_pop = []
        ihtimaller = [olasilik_hesabi(n, controls) for n in populasyon]
        for i in range(len(populasyon)):
            k1 = rnd_top(populasyon, ihtimaller) 
            k2 = rnd_top(populasyon, ihtimaller) 
            nesil = caprazlama(k1, k2)
            if random.random() < mutasyon_ihtimali:
                nesil = mutasyon(nesil)
            display(nesil)
            arr_yeni_pop.append(nesil)
            if controls(nesil) == max_c: break
        return arr_yeni_pop

    def display(k):
        yazdir.write("Kromozom = {},  Kontroller = {}"
            .format(str(k), controls(k)))
        yazdir.write("\n")
    
    yazdir=open("populasyon.txt","w")    
    if number=="8":
        nq=8
    elif number=="7":
        nq=7
    elif number=="6":
        nq=6
    elif number=="5":
        nq=5
    elif number=="4":
        nq=4
    max_c = (nq*(nq-1))/2 
    populasyon = [rnd_kromozom(nq) for _ in range(100)]
    kusak = 1
    while not max_c in [controls(krm) for krm in populasyon]:
        yazdir.write("=== Kuşak {} ===".format(kusak))
        yazdir.write("\n")
        populasyon = vezir_gen(populasyon, controls)
        yazdir.write(" ")
        yazdir.write("Max Kontrol = {}".format(max([controls(n) for n in populasyon])))
        yazdir.write("\n")
        kusak += 1
    arr_kromozom = []    
    yazdir.write("Çözülen Kuşak: {}!".format(kusak-1)) 
    yazdir.write("\n")
    for krm in populasyon:
        if controls(krm) == max_c:
            yazdir.write(" ")
            yazdir.write("Bulunan Çözüm: ")
            arr_kromozom = krm          
            display(krm)
            dosya=open("krom.txt","w")
            if nq==4 :
                dosya.write("S"+str(arr_kromozom[0])+str(arr_kromozom[1])+str(arr_kromozom[2])+str(arr_kromozom[3]))
            if nq==5 :
                dosya.write("S"+str(arr_kromozom[0])+str(arr_kromozom[1])+str(arr_kromozom[2])+str(arr_kromozom[3])+str(arr_kromozom[4]))
            if nq==6 :
                dosya.write("S"+str(arr_kromozom[0])+str(arr_kromozom[1])+str(arr_kromozom[2])+str(arr_kromozom[3])+str(arr_kromozom[4])+str(arr_kromozom[5]))
            if nq==7 :
                dosya.write("S"+str(arr_kromozom[0])+str(arr_kromozom[1])+str(arr_kromozom[2])+str(arr_kromozom[3])+str(arr_kromozom[4])+str(arr_kromozom[5])+str(arr_kromozom[6]))
            if nq==8 :
                dosya.write("S"+str(arr_kromozom[0])+str(arr_kromozom[1])+str(arr_kromozom[2])+str(arr_kromozom[3])+str(arr_kromozom[4])+str(arr_kromozom[5])+str(arr_kromozom[6])+str(arr_kromozom[7]))            
    chess_board = []
    for i in range(nq):
        chess_board.append(["x"] * nq)        
    for j in range(nq):
        chess_board[nq-arr_kromozom[j]][j]="Q"
        
    def display_chess(chess_board):
        for i in chess_board:
            yazdir.write(" ".join(i))
            yazdir.write("\n")            
    yazdir.write("\n")
    display_chess(chess_board)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
