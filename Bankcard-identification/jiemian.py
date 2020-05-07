import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(600, 400)
        self.setWindowTitle("银行卡识别v1.0")

        self.label = QLabel(self)
        self.label.setFixedSize(300, 200)
        self.label.move(100, 50)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(450, 130)
        btn.clicked.connect(self.openimage)

        btn = QPushButton(self)
        btn.setText("识别结果")
        btn.move(20, 300)

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(120, 300)
        self.textbox.resize(450, 30)
        self.textbox.setText('卡号：623052 0790013606467 银行：中国农业银行 类别：借记卡')

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())