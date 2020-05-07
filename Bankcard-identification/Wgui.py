#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/17 21:10
#@Author: hdq
#@File  : Wgui.py
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QFileDialog,QTextEdit
import sys

from qtpy import QtCore



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,400)
        self.setWindowTitle("银行卡识别")
        self.sellab1=QLabel("选择图片:")
        self.selline1=QLineEdit()
        self.selline1.setReadOnly(True)
        self.selbtn1=QPushButton("打开")

        self.piclabel1=QLabel("暂无图片")
        self.piclabel1.setStyleSheet("border:2px solid black")
        self.piclabel1.setFixedSize(380,200)
        self.piclabel1.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignHCenter)

        self.piclabel2 = QLabel("识别区域")
        self.piclabel2.setStyleSheet("border:2px solid black")
        self.piclabel2.setFixedSize(380, 50)
        self.piclabel2.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

        self.selbtn1.clicked.connect(self.selpic)
        hmainlayout = QHBoxLayout(self)

        mainlayout=QVBoxLayout(self)
        hlay1=QHBoxLayout(self)
        hlay1.addWidget(self.sellab1)
        hlay1.addWidget(self.selline1)
        hlay1.addWidget(self.selbtn1)
        mainlayout.addLayout(hlay1)

        mainlayout.addWidget(self.piclabel1)
        mainlayout.addWidget(self.piclabel2)
        hlay2=QHBoxLayout(self)
        self.regbtn=QPushButton("识别银行卡号码结果")
        self.regbtn.clicked.connect(self.recognizenumzone)
        hlay2.addStretch()
        hlay2.addWidget(self.regbtn)
        hlay2.addStretch()
        mainlayout.addLayout(hlay2)

        self.rltlab=QLabel("识别结果:")
        self.rltline=QLineEdit()
        self.rltline.setReadOnly(True)
        self.rltline.setFixedSize(200,20)
        hlay3=QHBoxLayout(self)
        hlay3.addStretch()
        hlay3.addWidget(self.rltlab)
        hlay3.addWidget(self.rltline)
        hlay3.addStretch()
        mainlayout.addLayout(hlay3)


        vlay1=QVBoxLayout(self)
        tiplab=QLabel("处理信息：")
        vlay1.addWidget(tiplab)
        self.showresult=QTextEdit()
        self.showresult.setReadOnly(True)
        vlay1.addWidget(self.showresult)

        hmainlayout.addLayout(mainlayout)
        hmainlayout.addLayout(vlay1)
        self.setLayout(hmainlayout)


    def showinfo(self,text):
        self.showresult.append(text+"\n")

    def selpic(self):
        self.showinfo("打开银行卡图片文件")
        name=QFileDialog.getOpenFileName(filter="Image Files(*.jpg *.png *.jpeg)")
        self.selline1.setText(name[0])
        #name[0]就是打开的文件名称
        # print(name)

    def recognizenumzone(self):
        #这是银行卡按钮的，点击识别的时候这里就会执行
        self.showinfo("识别银行卡号具体号码")

def show_window():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()